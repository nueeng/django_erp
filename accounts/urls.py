from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-in/', views.sign_in_view, name='sign-in'),
]