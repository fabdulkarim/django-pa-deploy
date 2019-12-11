from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Blog(models.Model):
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=140)
    content = models.CharField(max_length=500)
    #pass

class Mentor(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    experience = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    quotes = models.CharField(max_length=140)
    #pass

class Mentee(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=140)
    quotes = models.CharField(max_length=140)
    # pass