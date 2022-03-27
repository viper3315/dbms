from django.shortcuts import render
from .models import Order
from cart.models import Cart

def index(request):


    if request.method == 'POST':
        c = Cart.objects.values('title')
        user_id = request.POST['user_id']
        str = ""
        for car in c:
            str += car['title']
            # o = Order(title = str,user_id = user_id)
            # o.save()
    return render(request, 'pages/purchase.html')
