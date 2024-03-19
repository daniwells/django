from django.db import models
# from django import forms 

class Products(models.Model):
    
    VOLTAGE_CHOICES = (
        (110,'110V'),
        (220,'220V')
    )

    MARK_CHOICES = (
        ('Microsoft','Microsoft'),
        ('Apple','Apple'),
        ('Bosch','Bosch'),
        ('Samsumg','Samsumg'),
        ('Xiaomi','Xiaomi')
    )

    TYPE_CHOICES = (
        ('Portable','Portable'),
        ('Static','Static')
    )

    description = models.TextField()
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    amount = models.IntegerField()
    weight = models.DecimalField(max_digits = 5 , decimal_places = 2)
    volts = models.IntegerField( choices = VOLTAGE_CHOICES )
    voltage = models.CharField( choices = MARK_CHOICES, max_length = 10)
    type = models.CharField( choices = TYPE_CHOICES, max_length = 10 )


    def __str__(self):
        return self.name

# Create your models here.
