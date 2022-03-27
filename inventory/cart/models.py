from django.db import models

class Cart(models.Model):
    product_id = models.IntegerField(default = '0')
    title = models.CharField(max_length=200,default='none')
    qty = models.IntegerField(default = '0')
    user_id = models.IntegerField(blank = True)
    price = models.IntegerField(default = '0')
    def __str__(self):
        return self.title
