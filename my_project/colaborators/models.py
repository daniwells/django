from django.db import models

class Colaborator(models.Model):
    EDV = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=100)
    responsibillity = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    address = models.TextField()
    date_admission = models.DateField()
    schedule_start = models.TimeField()
    schedule_end = models.TimeField()
    perfil_image = models.CharField(max_length=100)

    def __str__(self):
        return self.name