from django.shortcuts import render

from main.models import Category, Product


def category(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Категории'
    }

    return render(request, "main/category.html", context)


def product(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
        'title': 'Продукты'
    }

    return render(request, "main/product.html", context)


def products(request, pk):
    products_list = Category.objects.get(pk=pk)
    context = {
        'products_list': Product.objects.filter(category=pk),
        'title': f'Продукты из выбранной категории {products_list.name}'
    }

    return render(request, "main/products.html", context)

