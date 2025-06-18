from django.db import models
from django.utils import timezone

# Create your models here.
class Distributor(models.Model):
    distributorid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=128)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username