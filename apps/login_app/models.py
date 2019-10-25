from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    surveyed = models.BooleanField(default=True) #whether or not the user has taken the survey. I know. It's ok.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
