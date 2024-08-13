from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserCheck(models.Model):
    userx = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)