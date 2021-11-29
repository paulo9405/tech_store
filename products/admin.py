from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'photo')


admin.site.register(Product, ProductAdmin)

# Register your models here.
