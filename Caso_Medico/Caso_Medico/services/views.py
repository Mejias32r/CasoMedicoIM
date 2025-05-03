from django.shortcuts import render
from django.apps import apps
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import *

# Create your views here.
# views.py
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/starter.html')

def query(request):
    return render(request, 'query/query.html')


def personalized(request):
    return render(request, 'dashboard/personalized.html')

def charge_csv(request):
    #Pablo pone el código aquí
    return 1

def get_graph_data(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    clase_x = request.GET.get('clase_x')
    atributo_x = request.GET.get('atributo_x')
    clase_y = request.GET.get('clase_y')
    atributo_y = request.GET.get('atributo_y')
    clase_z = request.GET.get('clase_z')
    atributo_z = request.GET.get('atributo_z')

    resultado = {}

    def obtener_datos_ordenados(clase, atributo):
        if not clase or not atributo:
            return None

        Modelo = apps.get_model('services', clase)

        if clase == "Patient":
            return list(Modelo.objects.order_by('job_number').values_list(atributo, flat=True))

        elif hasattr(Modelo, 'patient'):
            return list(
                Modelo.objects.select_related('patient')
                .order_by('patient__job_number')
                .values_list(atributo, flat=True)
            )
        elif hasattr(Modelo, 'patient_id'):
            return list(
                Modelo.objects.select_related('patient_id')
                .order_by('patient_id__job_number')
                .values_list(atributo, flat=True)
            )
        else:
            raise ValueError(f"El modelo {clase} no tiene relación clara con Patient")

    try:
        if clase_x and atributo_x:
            resultado["ejeX"] = obtener_datos_ordenados(clase_x, atributo_x)

        if clase_y and atributo_y:
            resultado["ejeY"] = obtener_datos_ordenados(clase_y, atributo_y)

        if clase_z and atributo_z:
            resultado["ejeZ"] = obtener_datos_ordenados(clase_z, atributo_z)

        if not resultado:
            return JsonResponse({'error': 'No se proporcionaron parámetros válidos'}, status=400)

        return JsonResponse(resultado)

    except LookupError:
        return JsonResponse({'error': 'Clase no encontrada'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



def parse_conditions(data, base_model='Patient'):
    """
    Construye un Q object recursivamente a partir del diccionario.
    """
    if "conditions" in data:
        connector = data.get("connector", "AND").upper()
        sub_qs = [parse_conditions(cond) for cond in data["conditions"]]
        q = sub_qs[0]
        for sub_q in sub_qs[1:]:
            q = q & sub_q if connector == "AND" else q | sub_q
        return q
    else:
        model_name = data["model"]
        attribute = data["attribute"]
        operator = data["operator"]
        value = data["value"]

        Model = apps.get_model("services", model_name)

        # El atributo es una relación hacia Patient en modelos secundarios
        if model_name != "Patient":
            field = f"{model_name.lower()}__{attribute}"
        else:
            field = attribute

        lookup_map = {
            "=": "",
            ">": "__gt",
            "<": "__lt",
            ">=": "__gte",
            "<=": "__lte",
            "!=": "__ne",  # Aunque Django no lo soporta directamente, podemos manejarlo aparte si hace falta
        }

        lookup = lookup_map.get(operator)
        if lookup is None:
            raise ValueError(f"Operador no soportado: {operator}")

        full_field = f"{field}{lookup}"
        print (f"Full field: {full_field}")
        return Q(**{full_field: value})


@csrf_exempt
@require_http_methods(["POST"])
def query_builder_view(request):
    if request.method != 'POST':
            return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)

    try:
        q_object = parse_conditions(data)
        patients = Patient.objects.filter(q_object).values_list('job_number', flat=True).distinct()
        return JsonResponse({'job_ids': list(patients)})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)