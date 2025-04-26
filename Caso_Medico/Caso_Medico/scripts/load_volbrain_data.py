import os
import sys
import django
import pandas as pd
# Estamos en: /Caso_Medico/Caso_Medico/scripts
# Necesitamos: /Caso_Medico (la carpeta que contiene el paquete `Caso_Medico`)
# Añadir la raíz del proyecto al sys.path (la carpeta que contiene manage.py)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Caso_Medico.settings")
django.setup() 
from Caso_Medico.services.models import (
    Patient, TissueMetrics, Cerebrum, Cerebellum, LateralVentricles, 
    Caudate, Putamen, Thalamus, GlobusPallidus, Hippocampus, Amygdala, Accumbens
)
from datetime import datetime
def borrar_datos():
    TissueMetrics.objects.all().delete()
    Patient.objects.all().delete()
    Cerebrum.objects.all().delete()
    Cerebellum.objects.all().delete()
    LateralVentricles.objects.all().delete()
    Caudate.objects.all().delete()
    Putamen.objects.all().delete()
    Thalamus.objects.all().delete()
    GlobusPallidus.objects.all().delete()
    Hippocampus.objects.all().delete()
    Amygdala.objects.all().delete()
    Accumbens.objects.all().delete()
def safe_float(value):
            try:
                if pd.isna(value):  # Si es NaN de pandas
                    return 0.0
                if isinstance(value, str):
                    value = value.replace(',', '.')
                return float(value)
            except (ValueError, TypeError):
                return 0.0

def insert_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    borrar_datos()
    print("Columnas encontradas en el Excel:", df.columns.tolist())
    for index, row in df.iterrows():
        patient, created = Patient.objects.get_or_create(
    job_number=row["Patient ID"],
    defaults={
        "sex": row["Sex"],
        "age": int(row["Age"]) if str(row["Age"]).isdigit() else None,
        "report_date": datetime.strptime(str(row["Report Date"]), "%d-%b-%Y").date() if isinstance(row["Report Date"], str) else row["Report Date"],
        "scale_factor": row["Scale factor"],
        "snr": row["SNR"],
        "msnr": row["mSNR"],
        "qc": row["QC"],
    },
)

        TissueMetrics.objects.create(
            patient_id=patient.job_number,
            tissue_wm_cm3=row['Tissue WM cm3'],
            tissue_wm_percentage=row['Tissue WM %'],
            tissue_gm_cm3=row['Tissue GM cm3'],
            tissue_gm_percentage=row['Tissue GM %'],
            tissue_csf_cm3=row['Tissue CSF cm3'],
            tissue_csf_percentage=row['Tissue CSF %'],
            tissue_brain_cm3=row['Tissue Brain cm3'],
            tissue_brain_percentage=row['Tissue Brain %'],
            tissue_ic_cm3=row['Tissue IC cm3'],
            tissue_ic_percentage=row['Tissue IC %']
        )

        Cerebrum.objects.create(
            patient_id=patient.job_number,
            total_cm3=row['Cerebrum Total cm3'],
            total_percentage=row['Cerebrum Total %'],
            t_gm_cm3=row['Cerebrum T GM cm3'],
            t_gm_percentage=row['Cerebrum T GM %'],
            t_wm_cm3=row['Cerebrum T WM cm3'],
            t_wm_percentage=row['Cerebrum T WM %'],
            right_cm3=row['Cerebrum Right cm3'],
            right_percentage=row['Cerebrum Right %'],
            left_cm3=row['Cerebrum Left cm3'],
            left_percentage=row['Cerebrum Left %'],
            asymmetry=row['Cerebrum Assymetry']
        )

        # Repite lo mismo con Cerebellum, LateralVentricles, Caudate, Putamen, etc.
        # por ejemplo:
        # Cerebellum.objects.create(...)
        # LateralVentricles.objects.create(...)
        # (Continuar igual con otros modelos)
        Cerebellum.objects.create(
            patient_id=patient.job_number,
            total_cm3=row['Cerebelum Total cm3'],
            total_percentage=row['Cerebelum Total %'],
            t_gm_cm3=row['Cerebelum T GM cm3'],
            t_gm_percentage=row['Cerebelum T GM %'],
            t_wm_cm3=row['Cerebelum T WM cm3'],
            t_wm_percentage=row['Cerebelum T WM %'],
            right_cm3=row['Cerebelum Right cm3'],
            right_percentage=row['Cerebelum Right %'],
            left_cm3=row['Cerebelum Left cm3'],
            left_percentage=row['Cerebelum Left %'],
            asymmetry=safe_float(row['Cerebelum Assymetry'])
        )

        LateralVentricles.objects.create(
            patient_id=patient.job_number,
            total_cm3=row['Lateral ventricles Total cm3'],
            total_percentage=row['Lateral ventricles Total %'],
            right_cm3=row['Lateral ventricles Right cm3'],
            right_percentage=row['Lateral ventricles Right %'],
            left_cm3=row['Lateral ventricles Left cm3'],
            left_percentage=row['Lateral ventricles Left %'],
            asymmetry=safe_float(row['Lateral ventricles Asymmetry'])
        )

        Caudate.objects.create(
            patient_id=patient.job_number,
            total_cm3=row['Caudate Total cm3'],
            total_percentage=row['Caudate Total %'],
            right_cm3=row['Caudate Right cm3'],
            right_percentage=row['Caudate Right %'],
            left_cm3=row['Caudate Left cm3'],
            left_percentage=row['Caudate Left %'],
            asymmetry=safe_float(row['Caudate Asymmetry'])
        )

        Putamen.objects.create(
            patient_id=patient.job_number,
            total_cm3=row['Putamen Total cm3'],
            total_percentage=row['Putamen Total %'],
            right_cm3=row['Putamen Right cm3'],
            right_percentage=row['Putamen Right %'],
            left_cm3=row['Putamen Left cm3'],
            left_percentage=row['Putamen Left %'],
            asymmetry=safe_float(row['Putamen Asymmetry'])
        )

        Thalamus.objects.create(
            patient_id=patient.job_number,
            total_cm3=row['Thalamus Total cm3'],
            total_percentage=row['Thalamus Total %'],
            right_cm3=row['Thalamus Right cm3'],
            right_percentage=row['Thalamus Right %'],
            left_cm3=row['Thalamus Left cm3'],
            left_percentage=row['Thalamus Left %'],
            asymmetry=safe_float(row['Thalamus Asymmetry'])
        )
        
        GlobusPallidus.objects.create(
            patient_id=patient.job_number,
            total_cm3=row['Globus Pallidus Total cm3'],
            total_percentage=row['Globus Pallidus Total %'],
            right_cm3=row['Globus Pallidus Right cm3'],
            right_percentage=row['Globus Pallidus Right %'],
            left_cm3=row['Globus Pallidus Left cm3'],
            left_percentage=row['Globus Pallidus Left %'],
            asymmetry=safe_float(row['Globus Pallidus Asymmetry'])
        )

        Hippocampus.objects.create(
            patient_id=patient.job_number,
            total_cm3=row['Hipocampus Total cm3'],
            total_percentage=row['Hippocampus Total %'],
            right_cm3=row['Hippocampus Right cm3'],
            right_percentage=row['Hippocampus Right %'],
            left_cm3=row['Hippocampus Left cm3'],
            left_percentage=row['Hippocampus Left %'],
            asymmetry=safe_float(row['Hippocampus Asymmetry'])
        )

        Amygdala.objects.create(
            patient_id=patient.job_number,
            total_cm3=row['Amygdala Total cm3'],
            total_percentage=row['Amygdala Total %'],
            right_cm3=row['Amygdala Right cm3'],
            right_percentage=row['Amygdala Right %'],
            left_cm3=row['Amygdala Left cm3'],
            left_percentage=row['Amygdala Left %'],
            asymmetry=safe_float(row['Amygdala Asymmetry'])
        )
        asymmetry_str = str(row['Accumbens Asymmetry,job_number,Patient ID'])[:4]
        asymmetry_str = asymmetry_str.replace(',', '.')
        try:
            asymmetry_value = float(asymmetry_str)
        except ValueError:
            asymmetry_value = 0.0
        Accumbens.objects.create(
            patient_id=patient.job_number,
            total_cm3=row['Accumbens Total cm3'],
            total_percentage=row['Accumbens Total %'],
            right_cm3=row['Accumbens Right cm3'],
            right_percentage=row['Accumbens Right %'],
            left_cm3=row['Accumbens Left cm3'],
            left_percentage=row['Accumbens Left %'],
            asymmetry=asymmetry_value,
        )
    print("¡Datos insertados con éxito!")

if __name__ == "__main__":
    excel_path = os.path.join(BASE_DIR, 'volbrain_data.xlsx') # Ruta real del archivo descargado
    insert_data_from_excel(excel_path)
