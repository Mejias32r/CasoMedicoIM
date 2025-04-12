from django.db import models

class Patient(models.Model):
    job_number = models.CharField(max_length=50, primary_key=True)
    sex = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("UNKNOWN", "UNKNOWN")])
    age = models.IntegerField(null=True, blank=True)
    report_date = models.DateField()
    scale_factor = models.FloatField()
    snr = models.FloatField()
    msnr = models.FloatField()
    qc = models.FloatField()
    
    def __str__(self):
        return f"Patient {self.job_number} ({self.sex}, {self.age} years)"

class TissueMetrics(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
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

class Cerebrum(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
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

class Cerebellum(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
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

class LateralVentricles(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

class Caudate(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

class Putamen(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

class Thalamus(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

class GlobusPallidus(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

class Hippocampus(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

class Amygdala(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()

class Accumbens(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    total_cm3 = models.FloatField()
    total_percentage = models.FloatField()
    right_cm3 = models.FloatField()
    right_percentage = models.FloatField()
    left_cm3 = models.FloatField()
    left_percentage = models.FloatField()
    asymmetry = models.FloatField()
