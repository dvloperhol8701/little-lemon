from django.db import models

# 1. Booking Table Model
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.BookingDate}"


# 2. Menu Table Model
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    inventory = models.IntegerField()

    # Updated to match Step 2 of the exercise instructions exactly
    def __str__(self):
        return f'{self.title} : {str(self.price)}'