from django.db import models
from django.conf import settings

class Item(models.Model):
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(decimal_places=2, max_digits=25)
    description = models.TextField()
    category = models.CharField(max_length=50)
    rating = models.IntegerField()
    offers = models.IntegerField()


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                            on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username


