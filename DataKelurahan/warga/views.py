from django.shortcuts import render
from django.views.generic import ListView
from .models import Warga

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
