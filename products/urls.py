from django.urls import path
from products.views import (
    create_product,
    list_products,
)

urlpatterns = [
    path('create_product/', create_product, name='create_products'),
    path('list_products/', list_products, name='list_products'),
]
