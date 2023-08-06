from rest_framework.test import APITestCase
from ..models import Note
from usermgmt.models import User
from django.urls import reverse
from rest_framework import status



class NoteViewTestCase(APITestCase):

    def setUp(self) :
        
        response = self.create_user()
        userId = response['id']
        noteObj1 = Note.objects.create(user_id = userId , title = 'lorem1',text='ipsum1')
        noteObj2 = Note.objects.create(user_id = userId , title = 'lorem2',text='ipsum2')
        
        self.noteObj = noteObj1
        self.accessToken = response['tokens']['access']
        self.headers = {'Authorization':f'Bearer {self.accessToken}'}
    
    def create_user(self):
        url = reverse('register')
        body = {
            'username':'aman',
            'email':'aman@gmail.com',
            'password':'Adminn123@'
        }
        response = self.client.post(url,body)
        if response.status_code == 201 :
            # accessToken = response.json()['tokens']['access']
            return response.json()
        else :
            print(f'register error :{response.content}')

    def test_create_note(self):
        url = '/api/note/'
        data = {
                "title":"fifth note",
                "text":"Lorem Ipsum is"
            }
    
        response = self.client.post(url,data,headers=self.headers,format='json')
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'],data['title'])

    def test_get_notes(self):
        url = '/api/note/'
        
        response = self.client.get(url,headers=self.headers)
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertTrue(len(response.json()),2)
        self.assertContains(response,self.noteObj.title)


    def test_get_note_details(self):
        noteId = self.noteObj.id
        url = f'/api/note/{noteId}/'
        
        response = self.client.get(url,headers=self.headers)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.json()['title'],self.noteObj.title)

    def test_get_note_details(self):
        noteId = self.noteObj.id
        url = f'/api/note/{noteId}/'
        
        data={'title':'lorem3'}
        response = self.client.patch(url,data,format='json',headers=self.headers)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.json()['title'],data['title'])
        self.assertEqual(response.json()['text'],self.noteObj.text)

    def test_delete_note(self):
        noteId = self.noteObj.id
        url = f'/api/note/{noteId}/'
        
        response = self.client.delete(url,headers=self.headers)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        



    
