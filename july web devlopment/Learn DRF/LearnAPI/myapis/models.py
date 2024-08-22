from django.db import models

# Create your models here.

class Contactus(models.Model):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self) -> str:
        return self.username