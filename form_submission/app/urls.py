from django.urls import path
from . import views
import requests

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup),
    path('login/', views.login),
    path('thanks/', views.thanks)
]
