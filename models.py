# real_estate/models.py
from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=[
        ('Platinum', 'Platinum'),
        ('Gold', 'Gold'),
        ('Silver', 'Silver')
    ])
    image = models.ImageField(upload_to='property_images/')

class Solicitor(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    verified = models.BooleanField(default=True)
