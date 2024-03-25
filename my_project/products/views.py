from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from .forms import ProductForm
from PIL import Image
import copy
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


def show_products(request):
    products = Products.objects.all()
    return render(request, 'products/show_products.html', {'products': products})

@csrf_exempt
def register_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        # print(request.POST)
        if form.is_valid():
            # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")    
            form.save()
            return redirect('products:show_products')
    else:
        form = ProductForm()
    return render(request, 'products/register_product.html', {'form': form})


def edit_product(request, pk):
    cliente = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('products:show_products')
    else:
        form = ProductForm(instance=cliente)
    return render(request, 'products/edit_product.html', {'form': form})

def delete_product(request, pk):
    cliente = get_object_or_404(Products, pk=pk)
    cliente.delete()
    return redirect('products:show_products')


# Create your views here.
