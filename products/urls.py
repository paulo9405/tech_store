from django.urls import path
from products.views import (
    create_product,
    list_products,
    update_product,
    delete_product
)

urlpatterns = [
    path('create-product/', create_product, name='create_products'),
    path('list-products/', list_products, name='list_products'),
    path('update-product/<int:id>/', update_product, name="update_product"),
    path('delete-product/<int:id>/', delete_product, name="delete_product"),
]
