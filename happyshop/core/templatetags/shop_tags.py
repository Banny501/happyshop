import logging

from django import template

register = template.Library()
logger = logging.getLogger(__name__)


# @register.inclusion_tag('core/main/_show_categories.html')
# def show_categories(cat_selected=0):
#     categories = Category.objects.annotate(Count('product'))
#     logger.error(categories)
#     return {"categories": categories, "cat_selected": cat_selected}
#
#
# @register.inclusion_tag('core/main/_show_products.html')
# def show_products(category=None):
#     if category:
#         products = Product.objects.filter(cat__slug=category)
#     else:
#         products = Product.objects.all()
#
#     return {"products": products}
#
