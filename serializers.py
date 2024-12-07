# real_estate/serializers.py
from rest_framework import serializers
from .models import Property, Solicitor

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class SolicitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitor
        fields = '__all__'
