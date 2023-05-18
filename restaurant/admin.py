from django.contrib import admin
from .models import Book,Menu

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "Name", "No_of_guest", "BookingDate"]

class MenuAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "price", "inventory"]

admin.site.register(Book, BookAdmin)
admin.site.register(Menu, MenuAdmin)