from django.db import models

class Patient(models.Model):
    job_number = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    report_date = models.DateField()
    scale_factor = models.FloatField()
    snr = models.FloatField()
    msnr = models.FloatField()
    qc = models.FloatField()
    class Meta:
        db_table = 'services_patient'  # Muy importante para enlazar con la tabla real
        managed = False  # Esto le dice a Django que NO debe tocar esta tabla con migraciones

class TissueMetrics(models.Model):
    patient_id = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='tissue_metrics')
    tissue_wm_cm3 = models.FloatField()
    tissue_wm_percentage = models.FloatField()
    tissue_gm_cm3 = models.FloatField()
    tissue_gm_percentage = models.FloatField()
    tissue_csf_cm3 = models.FloatField()
    tissue_csf_percentage = models.FloatField()
    tissue_brain_cm3 = models.FloatField()
    tissue_brain_percentage = models.FloatField()
    tissue_ic_cm3 = models.FloatField()
    tissue_ic_percentage = models.FloatField()
    class Meta:
        db_table = 'services_tissuemetrics'  # Muy importante para enlazar con la tabla real
        managed = False  # Esto le dice a Django que NO debe tocar esta tabla con migraciones
class Cerebrum(models.Model):
    patient_id = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='cerebrum')
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    t_gm_cm3 = models.FloatField()
    t_gm_percentage = models.FloatField()
    t_wm_cm3 = models.FloatField()
    t_wm_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()
    class Meta:
        db_table = 'services_cerebrum'
        managed = False

class Cerebellum(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, db_column='job_number')
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

    class Meta:
        db_table = 'services_cerebellum'
        managed = False

class LateralVentricles(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, db_column='job_number')
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

    class Meta:
        db_table = 'services_lateralventricles'
        managed = False

class Caudate(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, db_column='job_number')
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

    class Meta:
        db_table = 'services_caudate'
        managed = False

class Putamen(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, db_column='job_number')
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

    class Meta:
        db_table = 'services_putamen'
        managed = False

class Thalamus(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, db_column='job_number')
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

    class Meta:
        db_table = 'services_thalamus'
        managed = False

class GlobusPallidus(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, db_column='job_number')
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

    class Meta:
        db_table = 'services_globuspallidus'
        managed = False

class Hippocampus(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, db_column='job_number')
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

    class Meta:
        db_table = 'services_hippocampus'
        managed = False

class Amygdala(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, db_column='job_number')
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

    class Meta:
        db_table = 'services_amygdala'
        managed = False

class Accumbens(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, db_column='job_number')
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

    class Meta:
        db_table = 'services_accumbens'
        managed = False
