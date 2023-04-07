from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.sign_in_view, name='sign-in'), # name이 뭐지?
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('logout/', views.logout, name='logout'),
]