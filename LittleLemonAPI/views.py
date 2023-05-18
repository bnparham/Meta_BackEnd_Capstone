from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializer import MenuItemSerializer
from .models import MenuItem
# Create your views here.

class MenuItemsView(ListCreateAPIView):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()