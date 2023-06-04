from django.db import models
from usermgmt.models import User

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=500,blank=True)
    text = models.TextField(blank=True)
    theme = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        if self.title :
            return self.title
        else :
            return self.text[:50]