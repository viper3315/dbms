from django.db import models
from datetime import datetime


class Order(models.Model):
    title = models.CharField(max_length=5000, default = 'none')
    user_id = models.IntegerField(default="0")
    product_id = models.IntegerField(max_length=100)
    def __str__(self):
        return str(self.title)

