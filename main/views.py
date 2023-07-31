from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from main.models import Category, Product


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product


class ProductCategoryListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Продукты из выбранной категории {products_item.name}'
        return context_data


class ProductCardListView(ListView):
    model = Product
    template_name = 'main/blogentry_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset


# class BlogEntryDetailView(DetailView):
#     model = BlogEntry
#     # template_name = 'main/product_card.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object

# class ProductCreateView(CreateView):
#     model = Product
#     fields = ('name', 'price', 'photo', 'category',)
#     success_url = reverse_lazy('main:product')
