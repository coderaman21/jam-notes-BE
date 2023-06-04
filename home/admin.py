from django.contrib import admin
from .models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('user','title')
    list_filter = ('theme',)
    search_fields = ('user__email','text','title')
admin.site.register(Note,NoteAdmin)