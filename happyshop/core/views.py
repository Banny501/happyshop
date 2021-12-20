from django.views.generic import ListView, TemplateView

from .models import Product, Category
from .utils import DataMixin

TEMPLATE_NAME = "HappyShop"


class MainView(DataMixin, ListView):
    model = Product
    template_name = 'core/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=TEMPLATE_NAME)
        return dict(list(context.items()) + list(c_def.items()))


class ShopView(DataMixin, ListView):
    model = Category
    template_name = 'core/shop.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Shop - " + TEMPLATE_NAME,
                                      menu_selected="Shop")
        return dict(list(context.items()) + list(c_def.items()))


#
# class CategoryPage(DataMixin, DetailView):
#     model = Category
#     template_name = 'core/main/shop.html'
#     slug_url_kwarg = 'category_slug'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Shop - " + TEMPLATE_NAME,
#                                       category=self.kwargs.get(self.slug_url_kwarg, None),
#                                       cat_selected=context['category'].id,
#                                       menu_selected="Shop")
#         return dict(list(context.items()) + list(c_def.items()))
#
#
# class ProductPage(DataMixin, DetailView):
#     model = Product
#     slug_url_kwarg = 'product_slug'
#     context_object_name = 'product'
#     template_name = 'core/main/product.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title=str(context['product']) + " - " + TEMPLATE_NAME,
#                                       cat_selected=context['product'].cat_id,
#                                       menu_selected="Shop")
#         return dict(list(context.items()) + list(c_def.items()))
#
#
class AboutView(DataMixin, TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="About - " + TEMPLATE_NAME,
                                      menu_selected="About")
        return dict(list(context.items()) + list(c_def.items()))


class ContactView(DataMixin, TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Contact - " + TEMPLATE_NAME,
                                      menu_selected="Contact")
        return dict(list(context.items()) + list(c_def.items()))
