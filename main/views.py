

from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from main.form import ProductForm, VersionForm
from main.models import Category, Product, Version


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product

    @staticmethod
    def all_version():
        return Version.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['version_name'] = Version.objects.all()
    # #     # products_item = Category.objects.get(pk=self.kwargs.get('pk'))
    # #     # context_data['title'] = f'Продукты из выбранной категории {products_item.name}'
    #     return context_data




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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:product')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, fields=['name_version', 'name_current_version', ],
                                               extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


def toggle_activity(request, pk):
    product_item = get_object_or_404(Version, pk=pk)
    if product_item.name_current_version:
        product_item.name_current_version = False
    else:
        product_item.name_current_version = True

    product_item.save()

    return redirect(reverse('main:product'))
