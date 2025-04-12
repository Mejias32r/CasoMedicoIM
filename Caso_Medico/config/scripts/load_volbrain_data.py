import os
import sys
import django
import pandas as pd
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))      # .../Caso_Medico/Caso_Medico/scripts
PROJECT_DIR = os.path.dirname(CURRENT_DIR)                    # .../Caso_Medico/Caso_Medico
sys.path.append(PROJECT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Caso_Medico.settings")
django.setup()

from Caso_Medico.models import (
    Patient, TissueMetrics, Cerebrum, Cerebellum, LateralVentricles, 
    Caudate, Putamen, Thalamus, GlobusPallidus, Hippocampus, Amygdala, Accumbens
)

def insert_data_from_excel(file_path):
    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        patient = Patient.objects.create(
            job_number=row['Patient_ID'],
            sex=row['Sex'],
            age=row['Age'],
            report_date=row['Report_Date'],
            scale_factor=row['Scale_Factor'],
            snr=row['SNR'],
            msnr=row['mSNR'],
            qc=row['QC']
        )

        TissueMetrics.objects.create(
            patient_id=patient,
            tissue_wm_cm3=row['Tissue_WM_cm3'],
            tissue_wm_percentage=row['Tissue_WM_%'],
            tissue_gm_cm3=row['Tissue_GM_cm3'],
            tissue_gm_percentage=row['Tissue_GM_%'],
            tissue_csf_cm3=row['Tissue_CSF_cm3'],
            tissue_csf_percentage=row['Tissue_CSF_%'],
            tissue_brain_cm3=row['Tissue_Brain_cm3'],
            tissue_brain_percentage=row['Tissue_Brain_%'],
            tissue_ic_cm3=row['Tissue_IC_cm3'],
            tissue_ic_percentage=row['Tissue_IC_%']
        )

        Cerebrum.objects.create(
            patient_id=patient,
            total_cm3=row['Cerebrum_Total_cm3'],
            total_percentage=row['Cerebrum_Total_%'],
            t_gm_cm3=row['Cerebrum_T_GM_cm3'],
            t_gm_percentage=row['Cerebrum_T_GM_%'],
            t_wm_cm3=row['Cerebrum_T_WM_cm3'],
            t_wm_percentage=row['Cerebrum_T_WM_%'],
            right_cm3=row['Cerebrum_Right_cm3'],
            right_percentage=row['Cerebrum_Right_%'],
            left_cm3=row['Cerebrum_Left_cm3'],
            left_percentage=row['Cerebrum_Left_%'],
            asymmetry=row['Cerebrum_Asymmetry']
        )

        # Repite lo mismo con Cerebellum, LateralVentricles, Caudate, Putamen, etc.
        # por ejemplo:
        # Cerebellum.objects.create(...)
        # LateralVentricles.objects.create(...)
        # (Continuar igual con otros modelos)
        Cerebellum.objects.create(
            patient=patient,
            total_cm3=row['Cerebellum_total_cm3'],
            total_percentage=row['Cerebellum_total_%'],
            right_cm3=row['Cerebellum_right_cm3'],
            right_percentage=row['Cerebellum_right_%'],
            left_cm3=row['Cerebellum_left_cm3'],
            left_percentage=row['Cerebellum_left_%'],
            asymmetry=row['Cerebellum_asymmetry']
        )

        LateralVentricles.objects.create(
            patient=patient,
            total_cm3=row['LatVent_total_cm3'],
            total_percentage=row['LatVent_total_%'],
            right_cm3=row['LatVent_right_cm3'],
            right_percentage=row['LatVent_right_%'],
            left_cm3=row['LatVent_left_cm3'],
            left_percentage=row['LatVent_left_%'],
            asymmetry=row['LatVent_asymmetry']
        )

        Caudate.objects.create(
            patient=patient,
            total_cm3=row['Caudate_total_cm3'],
            total_percentage=row['Caudate_total_%'],
            right_cm3=row['Caudate_right_cm3'],
            right_percentage=row['Caudate_right_%'],
            left_cm3=row['Caudate_left_cm3'],
            left_percentage=row['Caudate_left_%'],
            asymmetry=row['Caudate_asymmetry']
        )

        Putamen.objects.create(
            patient=patient,
            total_cm3=row['Putamen_total_cm3'],
            total_percentage=row['Putamen_total_%'],
            right_cm3=row['Putamen_right_cm3'],
            right_percentage=row['Putamen_right_%'],
            left_cm3=row['Putamen_left_cm3'],
            left_percentage=row['Putamen_left_%'],
            asymmetry=row['Putamen_asymmetry']
        )

        Thalamus.objects.create(
            patient=patient,
            total_cm3=row['Thalamus_total_cm3'],
            total_percentage=row['Thalamus_total_%'],
            right_cm3=row['Thalamus_right_cm3'],
            right_percentage=row['Thalamus_right_%'],
            left_cm3=row['Thalamus_left_cm3'],
            left_percentage=row['Thalamus_left_%'],
            asymmetry=row['Thalamus_asymmetry']
        )

        GlobusPallidus.objects.create(
            patient=patient,
            total_cm3=row['GlobusPallidus_total_cm3'],
            total_percentage=row['GlobusPallidus_total_%'],
            right_cm3=row['GlobusPallidus_right_cm3'],
            right_percentage=row['GlobusPallidus_right_%'],
            left_cm3=row['GlobusPallidus_left_cm3'],
            left_percentage=row['GlobusPallidus_left_%'],
            asymmetry=row['GlobusPallidus_asymmetry']
        )

        Hippocampus.objects.create(
            patient=patient,
            total_cm3=row['Hippocampus_total_cm3'],
            total_percentage=row['Hippocampus_total_%'],
            right_cm3=row['Hippocampus_right_cm3'],
            right_percentage=row['Hippocampus_right_%'],
            left_cm3=row['Hippocampus_left_cm3'],
            left_percentage=row['Hippocampus_left_%'],
            asymmetry=row['Hippocampus_asymmetry']
        )

        Amygdala.objects.create(
            patient=patient,
            total_cm3=row['Amygdala_total_cm3'],
            total_percentage=row['Amygdala_total_%'],
            right_cm3=row['Amygdala_right_cm3'],
            right_percentage=row['Amygdala_right_%'],
            left_cm3=row['Amygdala_left_cm3'],
            left_percentage=row['Amygdala_left_%'],
            asymmetry=row['Amygdala_asymmetry']
        )

        Accumbens.objects.create(
            patient=patient,
            total_cm3=row['Accumbens_total_cm3'],
            total_percentage=row['Accumbens_total_%'],
            right_cm3=row['Accumbens_right_cm3'],
            right_percentage=row['Accumbens_right_%'],
            left_cm3=row['Accumbens_left_cm3'],
            left_percentage=row['Accumbens_left_%'],
            asymmetry=row['Accumbens_asymmetry']
        )
    print("¡Datos insertados con éxito!")

if __name__ == "__main__":
    excel_path = "/mnt/data/volbrain_data.xlsx"  # Ruta real del archivo descargado
    insert_data_from_excel(excel_path)
