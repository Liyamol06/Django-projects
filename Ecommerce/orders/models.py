from django.db import models
from customers.models import Customers
from products.models import Products

# Create your models here.
class Orders(models.Model):
    LIVE=1
    DELETE=0
    DELETE_STATUS=((LIVE, 'Live'), (DELETE, 'Delete'))
    INITIAL_CART=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSING=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    ORDER_STATUS=(
        (ORDER_PROCESSING, 'ORDER_PROCESSING'),
        (ORDER_DELIVERED, 'ORDER_DELIVERED'),
        (ORDER_REJECTED, 'ORDER_REJECTED'))
    user=models.ForeignKey(Customers, related_name="Orders", on_delete=models.SET_NULL, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    delete_status=models.IntegerField(default=LIVE, choices=DELETE_STATUS)
    order_status=models.IntegerField(default=INITIAL_CART, choices=ORDER_STATUS)

class OrderedItems(models.Model):
    product=models.ForeignKey(Products, related_name="Cart_lines", on_delete=models.SET_NULL, null=True)
    quantity=models.IntegerField(default=1)
    order=models.ForeignKey(Orders, related_name="Order", on_delete=models.CASCADE)
