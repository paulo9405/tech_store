from django.contrib import admin
from django.urls import path, include
from products.views import create_product
from django.conf import settings
from django.conf.urls.static import static

import products.models

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('product_photos', create_product, name='photo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
