from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Food, Event

class IndexView(generic.ListView):
    model = Food
    template_name = 'selectfood/index.html'

class EventView(generic.DetailView):
    model = Food
    template_name = 'selectfood/events.html'
