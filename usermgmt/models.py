from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,email,password,**other_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))

        email=self.normalize_email(email)
        user=self.model(email=email,**other_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**other_fields):
            other_fields.setdefault('is_staff',True)
            other_fields.setdefault('is_superuser',True)
            other_fields.setdefault('is_active',True)
            if other_fields.get('is_staff') is not True:
                raise ValueError('is_staff is set to False')
            if other_fields.get('is_superuser') is not True:
                raise ValueError('is_superuser is set to False')
            return self.create_user(email,password,**other_fields)


class User(AbstractBaseUser,PermissionsMixin):
    email         = models.EmailField(_('email address'),max_length=60,unique=True)
    username      = models.CharField(max_length=30,blank=True)
    date_joined   = models.DateTimeField(verbose_name='date_joined',auto_now_add=True)
    last_login    = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)

    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return  self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }