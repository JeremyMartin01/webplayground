from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class userCreationForWithEmail(UserCreationForm):
    email = forms.EmailField(required = True, help_text='campo requerido y debe ser válido')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El Email ya está registrado, prube con otro por favor")
        return email

class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'row':3, 'placeholder':'Biografia'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder':'Enlace'}),
        } 