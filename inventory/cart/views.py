from django.shortcuts import render,redirect
from .models import Cart

def cart(request):
    if request.method == 'POST':
        product_id = request.POST['pid']
        title = request.POST['name']
        qty = request.POST['qty']
        user_id = request.POST['user_id']
        price = request.POST['price']

        c = Cart(product_id = product_id, title = title, qty = qty, user_id = user_id, price = price)
        c.save()
        

        return redirect('/products/' + product_id)