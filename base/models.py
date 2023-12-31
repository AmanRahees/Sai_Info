from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField(null=False)
    date = models.DateField()
    status = models.BooleanField(default=False)