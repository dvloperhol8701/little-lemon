from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking  # <-- Imports both your Menu and Booking models

# 1. Menu Serializer (For your Menu API endpoints)
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']


# 2. User Serializer (For your User List endpoints)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        extra_kwargs = {
            'groups': {'required': False, 'default': []}
        }


# 3. Booking Serializer (New: For your Table Booking ModelViewSet)
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'