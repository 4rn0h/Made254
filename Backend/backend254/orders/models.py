from django.db import models

# Find on how to impliment this
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # The user who placed the order
    created_at = models.DateTimeField(auto_now_add=True) # The date and time when the order was created
    updated_at = models.DateTimeField(auto_now=True) # The date and time when the order was last updated
    status = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ), default='Pending') # Status of the order
    total_price = models.DecimalField(max_digits=10, decimal_places=2)# The total price of the order

    # add more fields to capture additional information about the order, such as shipping address, payment details, etc.

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
