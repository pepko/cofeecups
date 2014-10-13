from django.db import models

class Information_about_me(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateTimeField()
    bio = models.TextField(max_length = 10000, blank=True)
    contacts = models.CharField(max_length = 100, blank=True)
    email = models.EmailField(blank=True)
    jabber = models.CharField(max_length = 30, blank=True)
    skype = models.CharField(max_length = 30, blank=True)
    other_contacts = models.TextField(max_length = 10000, blank=True)
    
# Create your models here.
