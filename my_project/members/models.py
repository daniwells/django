from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    cpf = models.CharField(max_length=14)
    date_birth = models.DateField()

    def __str__(self):
        return self.name

# Create your models here.
