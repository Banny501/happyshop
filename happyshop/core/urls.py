from django.urls import path

from .views import ShopView, MainView, AboutView, ContactView, CategoryPage, ProductPage

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<slug:category_slug>/', CategoryPage.as_view(), name='category'),
    path('shop/<slug:category_slug>/<slug:product_slug>/', ProductPage.as_view(), name='product'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('card/', ContactView.as_view(), name='card'),
]
