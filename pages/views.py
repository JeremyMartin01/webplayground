from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, updateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Page

# Create your views here.
#Para cuando tengamos que devolver la lista de las instancias de un modelo
#ListView = Devolver una lista genérica y mostrarlo en un template
class PageListView(ListView):
    model=Page
   
#Para cuando tengamos que devolver unicamente una instancia de un modelo.
class PageDetailView(DetailView):
   model=Page

class PageCreate(CreateView):
    model=Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')
 
#Las vistas Delete y Update pero estas tenemos una primary key para recuperar las instancias.

class PageUpdate(CreateView):
    model=Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')