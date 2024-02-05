from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile

# Create your views here.
#ListView = Devolver una lista genérica y mostrarlo en un template
class ProfileListView(ListView):
    model = Profile # Usamos la clase Profile de la aplicación registration
    template_name = 'profiles/profile_list.html' # En este template mostramos la lista de perfiles
    paginate_by=3
class ProfileDetailView(DetailView): 
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])




    