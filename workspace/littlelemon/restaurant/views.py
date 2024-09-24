from django.shortcuts import render
from .serializers import SerializerMenu
from rest_framework import generics
from .models import Menu
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = SerializerMenu
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    ueryset = Menu.objects.all()
    serializer_class = SerializerMenu

def index(request):
    return render(request, 'index.html', {})
