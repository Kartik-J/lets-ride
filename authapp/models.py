from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)


    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
    def __str__(self):
        return f'{self.first_name} {self.last_name}'