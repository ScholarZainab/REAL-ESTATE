# Backend: Django - /real_estate/models.py
from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=[('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver')])
    image = models.ImageField(upload_to='property_images/')

class Document(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
    verified = models.BooleanField(default=False)
