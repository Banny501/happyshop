import logging

from core.models import Category, Product
from django import template
from django.db.models import Count

register = template.Library()
logger = logging.getLogger(__name__)


@register.inclusion_tag('layers/_show_menu.html')
def show_menu():
    return {"menu": [{'title': "Shop", 'url_name': 'shop'},
                     {'title': "About", 'url_name': 'about'},
                     {'title': "Contact", 'url_name': 'contact'},
                     ]}


@register.inclusion_tag('layers/_show_categories.html')
def show_categories(cat_selected=0):
    categories = Category.objects.annotate(Count('product'))
    return {"categories": categories, "cat_selected": cat_selected}


@register.inclusion_tag('layers/_show_products.html')
def show_products(category=None):
    if category:
        products = Product.objects.filter(cat__slug=category)
    else:
        products = Product.objects.all()

    return {"products": products}
#
