from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import User


# Create your tests here.
class UsermgmtTestCase(APITestCase):

    def setUp(self) -> None:
        self.email = 'admin@gmail.com'
        self.password = 'Admin231@'

        user = User(email=self.email,username='aman soni')
        user.set_password(self.password)
        user.save()
        self.user = user
    
    def test_create_user(self):
        url=reverse('register')
        data = {
            'username':'aman soni',
            'email':'admin@gmail.com',
            'password':'Admin321@'
        }
        response = self.client.post(url,data,format='json')
       
        self.assertNotEqual(response.status_code,status.HTTP_201_CREATED)
        data = {
            'username':'aman soni',
            'email':'aman@gmail.com',
            'password':'aDmin421@'
        }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'],data['email'])

    def test_login(self):
        url = reverse('login')
        data={'email':self.email,'password':self.password}
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        self.assertIn('access',response.json())
        self.assertIn('refresh',response.json())

        self.assertIsInstance(response.json()['access'],str)
        self.assertIsInstance(response.json()['refresh'],str)

        data={'email':self.email,'password':'admin231'}
        response = self.client.post(url,data,format='json')
        self.assertNotEqual(response.status_code,status.HTTP_200_OK)

class UserModelTestCase(TestCase):

    def test_create_user(self):
        username = 'aman soni'
        email = 'aman@gmail.com'
        password = 'aman431'
        user = User(email=email,username=username)
        user.set_password(password)
        user.save()

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):

        email = 'aman@gmail.com'
        password = 'aman431'

        superuser = User.objects.create_superuser(email = email , password=password)

        self.assertEqual(superuser.email,email)
        self.assertTrue(superuser.check_password(password))
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)