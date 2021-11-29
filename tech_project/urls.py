from django.contrib import admin
from django.urls import path
from products.models import Products
from django.conf import settings

import products.models

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('product_photos', Products, name='photo'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
