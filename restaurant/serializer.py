from rest_framework import serializers

from .models import Menu,Book

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
        depth = 1

class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "Name", "No_of_guest", "BookingDate"]
        depth = 1