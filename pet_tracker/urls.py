"""pet_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from pets.views import SinglePetView, DayView, AllPetsView, UpdateDosageView, ProductView, PetCreateView, ProductCreateView, \
    DosageDeleteView, ProductDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^$', DayView.as_view()),
    url(r'^pet/$', AllPetsView.as_view(), name='/pet'),
    url(r'^add_pet/', PetCreateView.as_view()),
    url(r'^pet/(?P<id>(\d)+)', SinglePetView.as_view()),
    url(r'^day/(?P<year>(\d){4})/(?P<month>(\d){1,2})/(?P<day>(\d){1,2})', DayView.as_view()),
    url(r'^day/$', DayView.as_view(), name='/day'),
    url(r'^add_product/$', ProductCreateView.as_view(), name='/add_product'),
    # url(r'^add_dosage/', DosageCreate.as_view()),
    url(r'^delete_dosage/(?P<pk>\d+)', DosageDeleteView.as_view()),
    url(r'^update_dosage/(?P<pk>\d+)', UpdateDosageView.as_view()),
    url(r'^product/(?P<id>\d+)', ProductView.as_view()),
    url(r'^delete_product/(?P<pk>\d+)', ProductDeleteView.as_view()),

]
