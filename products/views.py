from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()

    return redirect('list_products')


def list_products(request):
    products = Product.objects.all()
    form = ProductForm()
    data = {'products': products, 'form': form}
    return render(request, 'products/product.html', data)
