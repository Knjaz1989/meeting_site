from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    gender = models.TextField(verbose_name='Пол', choices=[('male', 'Мужской'), ('female', 'Женский')])
    icon = models.ImageField(verbose_name='Аватарка', upload_to='media/%Y/%m/%d', blank=True)