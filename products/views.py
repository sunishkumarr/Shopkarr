from django.shortcuts import render, get_object_or_404 
from .models import Category, Product

# Create your views here.
def product_list(request, category_id=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request, 'products/list.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, 'products/detail.html', context)