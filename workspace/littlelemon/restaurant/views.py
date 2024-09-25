from django.shortcuts import render
from .serializers import SerializerMenu, SerializerBooking
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = SerializerMenu

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    ueryset = Menu.objects.all()
    serializer_class = SerializerMenu

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = SerializerBooking