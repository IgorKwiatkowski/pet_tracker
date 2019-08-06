from django import forms
from .models import Pet, Product, Dosage, Unit
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class AddDosageForm(forms.Form):
        pet = forms.ModelChoiceField(queryset=Pet.objects.all(), label='Zwierzę')
        product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Produkt')
        amount = forms.DecimalField(max_digits=5, decimal_places=2, label='Ilość',
                                    help_text='Jednostka zależna od wybranego produktu')
        interval = forms.IntegerField(label='Co ile dni')
