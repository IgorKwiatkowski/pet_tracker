from django.db import models
from django.utils import timezone
import datetime

from django.template.backends import django


class Pet(models.Model):
    name = models.CharField(max_length=64, verbose_name='Imię')

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=32, verbose_name='Jednostka')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa')
    pets = models.ManyToManyField(Pet, through='Dosage',
                                  verbose_name='Zwierzę')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, verbose_name='jednostka')

    def __str__(self):
        return self.name


class Dosage(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name='Zwierzę')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Nazwa')
    amount = models.DecimalField(verbose_name='Ilość', max_digits=5,
                                 decimal_places=2)
    interval = models.IntegerField(verbose_name='Co ile dni')
    date_added = models.DateField(verbose_name='Od kiedy', default=timezone.now)
    notes = models.TextField(null=True, blank=True, verbose_name='Uwagi')

    def apply_on_day(self, day):
        delta = day - self.date_added
        return delta.days % self.interval == 0
