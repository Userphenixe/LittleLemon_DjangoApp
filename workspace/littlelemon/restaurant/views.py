from django.shortcuts import render
from .serializers import SerializerMenu, SerializerBooking
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu, Booking

def index(request):
    return render(request, 'index.html', {})
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = SerializerMenu
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    ueryset = Menu.objects.all()
    serializer_class = SerializerMenu

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = SerializerBooking