from core.models import Category, Product
from django import template
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('layers/_show_menu.html')
def show_menu(menu_selected=None):
    return {"menu_selected": menu_selected,
            "menu": [{'title': "Shop", 'url_name': 'shop'},
                     {'title': "About", 'url_name': 'about'},
                     {'title': "Contact", 'url_name': 'contact'},
                     ]}


@register.inclusion_tag('layers/_show_categories.html')
def show_categories(cat_selected=None):
    categories = Category.objects.annotate(Count('product'))
    return {"categories": categories, "cat_selected": cat_selected}


@register.inclusion_tag('layers/_show_products.html')
def show_products(category=None, limit=None):
    if category:
        products = Product.objects.filter(cat__slug=category)[:limit]
    else:
        products = Product.objects.all()[:limit]

    return {"products": products}
#
