from django.db import models
from djrichtextfield.models import RichTextField


# Create your models here.
class Testimony(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = RichTextField()

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email