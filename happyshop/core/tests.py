from core.models import Product, Category
from django.test import TestCase


class ProductTestCase(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name="TestCategory", slug="testslug")
        Product.objects.create(name="First_Product",
                               price=10,
                               cat=Category.objects.get(name="TestCategory"),
                               slug="testproductslug")

    def test_product_test(self):
        product = Product.objects.get(name="First_Product")
        self.assertEqual(product.get_price(), "10.0 ₿")
        self.assertEqual(product.get_absolute_url(), "/shop/testslug/testproductslug/")

