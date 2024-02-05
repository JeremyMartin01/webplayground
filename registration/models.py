from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

#Permitimos que un usuario unicamente tenga un solo avatar, y lo demas lo borramos, en otras palabras cuando el usuario  cambie su avatar la anterior siempre se va a borrar
def custon_upload_to(instance, filename):    
    old_instance = Profile.objects.get(pk=instance.pk)#recuperar la instancia justo antes de guardarla
    old_instance.avatar.delete() #Eliminami avatar anterior
    return 'profile/' + filename

# Create your models here.
class Profile(models.Model):
    #No se puede tener 2 perfiles para un mismo usuario, ni un mismo perfil para distintos usuarios
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar =  models.ImageField(upload_to=custon_upload_to,null=True, blank=True)
    bio = models.TextField(null= True, blank=True)
    link = models.URLField(max_length=200, null= True, blank=True)

    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exist(instance, **kwargs):
    if kwargs.get('create', False):
        Profile.objects.get_or_create(user=instance)
        #print("Se acaba de crear un usuario y su perfil enlazado")