from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    USER_ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
    )
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES)