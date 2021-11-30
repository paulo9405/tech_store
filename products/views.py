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


def update_product(request, id):
    data = {}
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    data['product'] = product
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        return render(request, 'products/update_product.html',  data)


def delete_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('list_products')
    else:
        return render(request, 'products/delete_confirm.html', {'obj': product})
