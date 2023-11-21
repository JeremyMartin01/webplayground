from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page

# Create your views here.
#Para cuando tengamos que devolver la lista de las instancias de un modelo
#ListView = Devolver una lista genérica y mostrarlo en un template
class pageLisView(ListView):
    model=Page
   
#Para cuando tengamos que devolver unicamente una instancia de un modelo.
class PageDetailView(DetailView):
   model=Page