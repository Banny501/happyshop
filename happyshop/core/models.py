from django.db import models
from django.urls import reverse

BITCOIN_SYMBOL = u"\u20BF"


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    old_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Старая Цена", blank=True, null=True)
    sale = models.BooleanField(default=False, verbose_name="Скидка")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="products/", verbose_name="Фото")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    updated = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    stock = models.BooleanField(default=False, verbose_name="Наличие")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['created', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'category_slug': Category.objects.get(id=self.cat_id).slug,
                                          'product_slug': self.slug})

    def get_price(self):
        return "{:.1f} ".format(self.price) + BITCOIN_SYMBOL


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
