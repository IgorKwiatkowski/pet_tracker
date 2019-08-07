from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Product, Pet, Unit, Dosage
from .forms import AddDosageForm
from django.utils.dateparse import parse_date
from datetime import date


class SinglePetView(View):
    def get(self, request, id):
        pet = Pet.objects.get(id=id)
        context = {'dosages': Dosage.objects.filter(pet=pet),
                   'pet': pet,
                   'form': AddDosageForm(initial={'pet': pet})}
        return render(request, 'single_pet.html', context)

    def post(self, request, id):
        form = AddDosageForm(request.POST)
        if form.is_valid():
            pet = form.cleaned_data['pet']
            product = form.cleaned_data['product']
            amount = form.cleaned_data['amount']
            interval = form.cleaned_data['interval']
            new_dosage = Dosage.objects.create(pet=pet,
                                               product=product,
                                               amount=amount,
                                               interval=interval)
            return HttpResponseRedirect(self.request.path_info)
        else:
            return HttpResponse('babol w formularzu!')


class AllPetsView(View):
    def get(self, request):
        pets = Pet.objects.all()
        context = {'pets': pets}
        return render(request, 'all_pets.html', context)


class ProductView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        dosages = Dosage.objects.filter(product=product)
        consumption = 0
        for dosage in dosages:
            rate = float(dosage.amount) * (1 / dosage.interval)
            consumption += rate
        return render(request, 'product.html', {'product': product, 'dosages': dosages, 'consumption': consumption})


class DayView(View):
    today = date.today()

    def get(self, request, year=today.year, month=today.month, day=today.day):
        date = parse_date(f'{year}-{month}-{day}')
        dosages = []
        pets = Pet.objects.all()
        for item in Dosage.objects.order_by('pet__name'):
            if item.apply_on_day(date):
                dosages.append(item)
        context = {'dosages': dosages,
                   'date': date,
                   'pets': pets}
        return render(request, 'day.html', context)


class PetCreate(CreateView):
    model = Pet
    fields = ['name']
    success_url = reverse_lazy('/pet')


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'unit']
    success_url = reverse_lazy('/day')


class DeleteDosageView(DeleteView):
    model = Dosage
    success_url = '/day'


class UpdateDosageView(UpdateView):
    model = Dosage
    fields = ['pet', 'product', 'amount', 'interval']
    template_name = 'pets/dosage_form.html'
    success_url = '/day'
