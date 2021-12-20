from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'old_price', 'stock', 'sale')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_editable = ('stock', 'sale')
    list_filter = ('cat', 'stock', 'sale', 'created')
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
