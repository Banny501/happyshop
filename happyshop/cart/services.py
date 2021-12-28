from decimal import Decimal

from core.models import Product
from django.conf import settings
from django.shortcuts import get_object_or_404


class Cart(object):
    def __init__(self, request):
        """
        Initial cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Looping products the items in the cart and getting products from the database.
        """
        product_slugs = self.cart.keys()
        products = Product.objects.filter(slug__in=product_slugs)
        for product in products:
            self.cart[str(product.slug)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Counting items in the cart.
        """
        return len(self.cart.values())

    def save(self):
        """
        Save carts to session
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product_slug, quantity=1, update_quantity=False):
        """
        Add a product to cart or update its quantity.
        """
        product = get_object_or_404(Product, slug=product_slug)

        if product_slug not in self.cart:
            self.cart[product_slug] = {'quantity': 0,
                                       'price': str(product.price)}
        if update_quantity:
            self.cart[product_slug]['quantity'] = quantity
        else:
            self.cart[product_slug]['quantity'] += quantity
        self.save()

    def delete(self, product_slug):
        """
        Removing an item from the cart.
        """
        if product_slug in self.cart:
            del self.cart[product_slug]
            self.save()

    def clear(self):
        """
        Deleting trash from session
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        """
        Calculation of the cost of products in the cart.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())
