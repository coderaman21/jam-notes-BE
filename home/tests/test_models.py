from django.test import TestCase
from ..models import Note
from usermgmt.models import User

class NoteTestCase(TestCase):

    def create_user(self):
        user = User(email='aman@gmail.com',username='aman soni')
        user.set_password('aman4213')
        user.save()
        
        return user

    def test_create_note(self):
        user = self.create_user()

        title = 'lorem isoum'
        text = 'lorem isoum'

        note = Note.objects.create(user = user ,title = title , text = text)
        self.assertEqual(note.title,title)
        self.assertEqual(note.text,text)
        self.assertEqual(note.user,user)
