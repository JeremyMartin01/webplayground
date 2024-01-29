from django.test import TestCase
from  .models import Profile
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        #Crear un usuario de prueba
        User.objects.create_user('ejemplo', 'ejemplo@hotmail.com', 'Qweuio125')
        

    def test_profile_exists(Self):
        exists = Profile.objects.filter(user__username='ejemplo').exists()
        Self.assertEqual(exists, True)