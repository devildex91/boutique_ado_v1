from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
# Create your views here.

from django.shortcuts import render

# Create your views here.
def all_products(request):
    """ A view to show individual product details"""

    products = Product.objects.all()

    if request.GET:
        if 'q' in request.GET:
            query= request.GET['q']
            if not query:
                messages.error(request, "You diddnt enter any search criteria!")
                return redirect(reverse('products'))


    context = {
        'products' : products,
    }


     
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show all products, including sorting and search queries"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }


     
    return render(request, 'products/product_detail.html', context)