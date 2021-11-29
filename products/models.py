from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    photo = models.ImageField(upload_to='product_photos', blank=True)

    def __str__(self):
        return self.name
