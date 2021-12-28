from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('shop/<slug:category_slug>/', views.CategoryView.as_view(), name='category'),
    path('shop/<slug:category_slug>/<slug:product_slug>/', views.ProductView.as_view(), name='product'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
