from django.db import models
from datetime import datetime

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

class Book(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guest = models.IntegerField(max_length=6)
    BookingDate = models.DateTimeField(default=datetime.now())