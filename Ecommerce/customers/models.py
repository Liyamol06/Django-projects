from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customers(models.Model):
    LIVE=1
    DELETE=0
    DELETE_STATUS=((LIVE, 'Live'), (DELETE, 'Delete'))
    name=models.CharField(max_length=200)
    user=models.OneToOneField(User, related_name='Customer_detail', 
                                on_delete=models.CASCADE)
    address=models.TextField()
    phone=models.IntegerField()
    email=models.EmailField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    delete_status=models.IntegerField(default=LIVE, choices=DELETE_STATUS)

    def __str__(self):
        return self.name