from cafemenu.models import MenuItem


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        # session = {'cart':{}}
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, product, quantity=1, replace_current_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # cart = Cart(request)
    # cart.add(p10,1)
    # cart.add(p10,5)
    # for item in cart:

    def __iter__(self):
        product_ids = self.cart.keys()
        # (id__in=[1,20,23])
        products = MenuItem.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item

        # cart = {
        #     product_id=1 : {  'quantity': quantity,
        #                      'product_obj': product },
        #
        #     product_id = 20: { 'quantity': quantity,
        #                       'product_obj': product },
        #
        #    product_id = 23: { 'quantity': quantity,
        #                    'product_obj': product },
        #      }

    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        # products = MenuItem.objects.filter(id__in=product_ids)
        # return sum([product.price for product in products])
        return sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())

