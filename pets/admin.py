from django.contrib import admin
from .models import Product, Pet, Dosage, Unit


admin.site.register(Product)
admin.site.register(Pet)
admin.site.register(Dosage)
admin.site.register(Unit)
