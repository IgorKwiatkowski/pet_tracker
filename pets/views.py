from django.shortcuts import render
from django.views import View
from .models import Product, Pet, Unit, Dosage
import datetime


class SinglePetView(View):
    def get(self, request, id):
        pet = Pet.objects.get(id=id)
        context = {'dosages': Dosage.objects.filter(pet=pet),
                   'pet': pet}
        return render(request, 'single_pet.html', context)

