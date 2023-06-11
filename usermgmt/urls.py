from django.urls import path
from rest_framework_simplejwt.views import (
   
    TokenRefreshView,
)
from .views import LoginViewSet,RegisterViewSet

urlpatterns = [
    path('login/',LoginViewSet.as_view(),name='login'),
    path('register/',RegisterViewSet.as_view(),name='register'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]