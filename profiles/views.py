from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
#ListView = Devolver una lista genérica y mostrarlo en un template
class ProfileListView(ListView):
    model = Page