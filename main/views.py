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


def products_categories(request, pk):
    products_item = Category.objects.get(pk=pk)
    context = {
        'product_list': Product.objects.filter(category=pk),
        'title': f'Продукты из выбранной категории {products_item.name}'
    }

    return render(request, "main/products_categories.html", context)


def product_card(request, name):
    products_item = Product.objects.get(name=name)
    context = {
        'product_list': Product.objects.filter(name=name),
        'title': f'Полное описание продукта {products_item.name}'
    }

    return render(request, "main/product_card.html", context)
