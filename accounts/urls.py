from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('Services/', views.Services),
    path('Login/', views.Login),
]