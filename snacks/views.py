from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView

from .models import snacks


class HomeView(TemplateView):
  template_name='home.html'


class SnackView(ListView):
    template_name='snacks_list.html'
    model=snacks


class SnackDetails(DetailView):
    template_name='snacks_details.html'
    model=snacks
