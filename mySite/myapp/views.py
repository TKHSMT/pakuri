from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Person
 
class SampleAppList(ListView):
    template_name = 'list.html'
    model = Person
