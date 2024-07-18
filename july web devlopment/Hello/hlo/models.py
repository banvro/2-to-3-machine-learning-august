from django.db import models

# Create your models here.

class ContactUs(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.CharField(max_length=50) 
    phone_number = models.IntegerField()
    message = models.TextField()


# python manage.py makemigrations
# python manage.py migrate
