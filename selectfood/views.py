from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Food, Event

class IndexView(generic.ListView):
    template_name = 'selectfood/index.html'
    model = Food
