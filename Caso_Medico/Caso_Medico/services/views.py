from django.shortcuts import render
from django.apps import apps
from django.http import JsonResponse

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
    if request.method == 'GET':
        clase_x = request.GET.get('clase_x')
        atributo_x = request.GET.get('atributo_x')
        clase_y = request.GET.get('clase_y')
        atributo_y = request.GET.get('atributo_y')

        try:
            # Obtener los modelos dinámicamente
            ModeloX = apps.get_model('services', clase_x)
            ModeloY = apps.get_model('services', clase_y)

            # Obtener datos
            datos_x = list(ModeloX.objects.values_list(atributo_x, flat=True))
            datos_y = list(ModeloY.objects.values_list(atributo_y, flat=True))

            return JsonResponse({
                "ejeX": datos_x,
                "ejeY": datos_y
            })

        except LookupError:
            return JsonResponse({'error': 'Clase no encontrada'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)