from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, Menu

class SerializerMenu(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
        extra_kwargs = {'price': {'min_value': 2},
                        'inventory': {'min_value': 0}}
        
class SerializerBooking(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'no_of_guests', 'bookingDate']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']