from asyncio.windows_events import NULL
from django.db import models
from django.utils import timezone
from seller.models import Seller
from datetime import datetime

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    product_id = models.IntegerField()
    product_img = models.ImageField(default = NULL)
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    description = models.TextField(blank = True)
    img_inside1 = models.ImageField(blank = True)
    img_inside2 = models.ImageField(blank = True)
    img_inside3 = models.ImageField(blank = True)
    img_inside4 = models.ImageField(blank = True)
    img_inside5 = models.ImageField(blank = True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default = datetime.now(), blank = True)
    def __str__(self):
        return self.title