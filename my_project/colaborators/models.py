from django.db import models

class Colaborator(models.Model):
    EDV = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=100)
    responsibillity = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    address = models.TextField()
    schedule_work = models.TimeField()
    date_start = models.DateField()
    date_end = models.DateField()
    perfil_image = models.CharField(max_length=100)

    def __str__(self):
        return self.name