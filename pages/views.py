<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page

# Create your views here.
def pages(request):
    pages = get_list_or_404(Page)
    return render(request, 'pages/pages.html', {'pages':pages})

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page.html', {'page':page})
=======
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
>>>>>>> 7be700f87883979e0e370f0c07dbb6b8052f9dda
