# Create your views here.
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from .forms import userCreationForWithEmail, Profileform, EmailForm
from django.views.generic import CreateView
#from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

class SignUpView(CreateView):
    form_class = userCreationForWithEmail
    success_url = reverse_lazy('login')
    template_name ='registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') +'?register'
    
    def get_form(self, form_class=None):
        form = super (SignUpView, self).get_form()
        #Modificamos el form en tiempo real con widgets
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form_control mb-2','placeholder':'Nombre de Usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form_control mb-2','placeholder':'Dirección Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form_control mb-2','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form_control mb-2','placeholder':'Confirmar Contraseña'})
        #form.fields['username'].label  
        return form
#Solamente es accesible cuando el usuario esta autentificado

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = Profileform   
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html' 
    #Recuperar el perfil a traves del identificador del usuario que hay en request
    def get_object(self):
        #conseguir o crear a parit del filtro , si no existe lo crea
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm   
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html' 
    #Recuperar el perfil a traves del identificador del usuario que hay en request
    
    def get_object(self):  
        #Recuperar el objeto que se va a editar     
        return self.request.user #Recuperamos la instancia del usuario

    def get_form(self, form_class=None):
        form = super (EmailUpdate, self).get_form()
        #Modificamos el form en tiempo real con widgets
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form_control mb-2','placeholder':'Email'})
                
        return form