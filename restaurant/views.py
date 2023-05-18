from django.shortcuts import render
from django.views import View
from .serializer import MenuItemSerializer
from .models import Book,Menu
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

class index(View):
    def get(self, request):
        context = {}
        return render(request, "index.html", context)


class MenuItemsView(ListCreateAPIView):
    serializer_class = MenuItemSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]