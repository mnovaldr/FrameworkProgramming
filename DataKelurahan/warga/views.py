from django.shortcuts import render
from django.views.generic import ListView, DetailView  
from .models import Warga

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
