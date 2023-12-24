from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.cart import Cart


@login_required
def order_create_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        new_order = Order(user=request.user, is_paid=True)
        new_order.save()

        for item in cart:
            product = item["product_obj"]
            OrderItem.objects.create(
                order=new_order,
                product=product,
                quantity=item['quantity'],
                price=product.price,
            )
        cart.clear()
        return redirect('cafemenu:home')
    else:
        print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
        return render(request, 'orders/orders_create.html')
