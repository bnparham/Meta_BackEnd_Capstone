from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import MenuItemSerializer
from .models import MenuItem
# Create your views here.

class MenuItemsView(ListCreateAPIView):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    permission_classes = [IsAuthenticated]