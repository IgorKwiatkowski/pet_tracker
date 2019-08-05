from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Product, Pet, Unit, Dosage
from django.utils.dateparse import parse_date
import datetime


class SinglePetView(View):
    def get(self, request, id):
        pet = Pet.objects.get(id=id)
        context = {'dosages': Dosage.objects.filter(pet=pet),
                   'pet': pet}
        return render(request, 'single_pet.html', context)


class DayView(View):
    def get(self, request, year, month, day):
        date = parse_date(f'{year}-{month}-{day}')
        dosages = []
        for item in Dosage.objects.all():
            if item.apply_on_day(date):
                dosages.append(item)
        context = {'dosages': dosages,
                   'date': date}
        return render(request, 'day.html', context)