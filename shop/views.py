from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    categories = Category.objects.all()  # Все категории для сайдбара
    products = Product.objects.filter(available=True)
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/list.html', {
        'categories': categories,
        'category': category,  # Важно передать текущую категорию!
        'products': products,
    })


def product_detail(request, pk, slug):
    product = get_object_or_404(Product,
                                pk=pk,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})
