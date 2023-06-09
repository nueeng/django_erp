from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('inventory', views.erp_home, name='inventory') # 127.0.0.1:8000/tweet 과 views.py 폴더의 tweet 함수 연결
]