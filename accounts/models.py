from django.contrib.auth.models import AbstractUser, User
from django.db import models
import uuid

class CustomUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.email
