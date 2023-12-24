from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from cafemenu.models import MenuItem
from .forms import AddToCartProductForm


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def add_to_cart_view(request, details_id):
    cart = Cart(request)

    product = get_object_or_404(MenuItem, id=details_id)
    form = AddToCartProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        quantity = cd['quantity']
        cart.add(product, quantity, replace_current_quantity=cd['inplace'])
        return redirect('cart:cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(MenuItem, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

