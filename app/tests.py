from django.test import TestCase,Client
import app.models as _
from .views import *
from django.db.utils import IntegrityError
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserTestCase(TestCase):

    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser(
            username='heidy', name="Heidy",  apellidos="Miranda", ci="96090512205", tfno="+5356562172", password='12345678')
        self.user = get_user_model().objects.create_user(
            username='admin', name="Admin",  apellidos="Admin", ci="96090512206", tfno="+5356562173", password='12345678')
        
    def test_User_create(self):
        superuser = _.User.objects.get(username='heidy')
        user = _.User.objects.get(username='admin')
        self.assertEqual(superuser.username, 'heidy')
        self.assertEqual(user.username, 'admin')
        
    def test_User_edit(self):
        user = User.objects.get(username="admin")
        user.username = 'editado'
        user.save()
        self.assertEqual(user.username, 'editado')
        
    def test_User_delete(self):
        # Los Usuarios son borrados correctamente
        self.client.login(username='heidy', password='12345678')
        response = self.client.delete(reverse('eliminar_user',kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/Usuario/'))
    
    def test_create_User_con_campos_vacios(self):
        with self.assertRaises(IntegrityError):
             User.objects.create_user(
            username='None', name=None,  apellidos=None, ci=None, tfno=None, password=None)

    def test_delete_User_no_existente(self):
        with self.assertRaises(_.User.DoesNotExist):
            User.objects.get(pk="10")

class LocalTestCase(TestCase):
    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser(
            username='heidy', name="Heidy",  apellidos="Miranda", ci="96090512205", tfno="+5356562172", password='12345678')
        self.user = get_user_model().objects.create_user(
            username='admin', name="Admin",  apellidos="Admin", ci="96090512206", tfno="+5356562173", password='12345678')
        self.local = _.Local()
        self.local.nombre="Aula 101"
        self.local.tipo = 'A'
        self.local.save()
    
    def test_create_local(self):
        self.client.login(username='heidy', password='12345678')
        response = self.client.post(reverse('add_local'), {'nombre':'Aula 105','tipo': 'A'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/local/'))
        Created = _.Local.objects.get(nombre="Aula 105")
        self.assertIsInstance(Created,_.Local)
        self.assertEqual(Created.nombre, 'Aula 105')
        
    def test_edit_local(self):
        self.client.login(username='heidy', password='12345678')
        response = self.client.post(reverse('editar_local', kwargs={'pk': self.local.pk}), {'nombre':'Aula 102','tipo': 'A'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/local/'))
        Created = _.Local.objects.get(nombre="Aula 102")
        self.assertIsInstance(Created,_.Local)
        self.assertEqual(Created.nombre, 'Aula 102')

    def test_local_delete(self):
        # Los Usuarios son borrados correctamente
        self.client.login(username='heidy', password='12345678')
        response = self.client.delete(reverse('eliminar_local',kwargs={'pk': self.local.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/local/'))
    
    def test_create_local_con_campos_vacios(self):
        with self.assertRaises(IntegrityError):
             Local.objects.create(nombre=None,tipo=None)

    def test_delete_local_no_existente(self):
        with self.assertRaises(Local.DoesNotExist):
            Local.objects.get(pk="10")


    