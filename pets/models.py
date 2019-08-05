from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=64, verbose_name='Imię')


class Unit(models.Model):
    name = models.CharField(max_length=32, verbose_name='Jednostka')


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa')
    pets = models.ManyToManyField(Pet, through='Dosage',
                                  verbose_name='Zwierzę')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)


class Dosage(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name='Zwierzę')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Nazwa')
    amount = models.DecimalField(verbose_name='Dawkowanie', max_digits=5,
                                 decimal_places=2)
    time_interval = models.IntegerField(verbose_name='Co ile dni')
