from django.db import models
from django.contrib.auth.models import User 

class Products(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE, 'Live'), (DELETE, 'Delete'))
    name=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to="media/products/", null=True, blank=True)
    priority=models.IntegerField(default=0)
    deleted_status=models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(
                                User,  
                                on_delete=models.CASCADE, 
                                related_name='created_product', 
                                default=1)

    def __str__(self):
        return self.name
