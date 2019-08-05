from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .models import Product, Pet, Unit, Dosage
from django.utils.dateparse import parse_date
import datetime
from datetime import date


class SinglePetView(View):
    def get(self, request, id):
        pet = Pet.objects.get(id=id)
        context = {'dosages': Dosage.objects.filter(pet=pet),
                   'pet': pet}
        return render(request, 'single_pet.html', context)


class AllPetsView(View):
    def get(self, request):
        pets = Pet.objects.all()
        context = {'pets': pets}
        return render(request, 'all_pets.html', context)

class DayView(View):
    today = date.today()

    def get(self, request, year=today.year, month=today.month, day=today.day):
        date = parse_date(f'{year}-{month}-{day}')
        dosages = []
        for item in Dosage.objects.all():
            if item.apply_on_day(date):
                dosages.append(item)
        context = {'dosages': dosages,
                   'date': date}
        return render(request, 'day.html', context)


class PetCreate(CreateView):
    model = Pet
    fields = ['name']
    success_url = reverse_lazy('/pet')
