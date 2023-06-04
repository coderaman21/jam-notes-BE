from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','username','last_login')
    list_filter = ('is_active',)
    search_fields = ('email','username')
admin.site.register(User,UserAdmin)
