from django.db import models
from django.contrib.auth.models import AbstractUser # 장고 기본 모델 가져오기

# Create your models here.

class AccountModel(AbstractUser):
    class Meta:
        db_table = "my_account"

    name = models.TextField(max_length=50, blank=True)
