from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from main.form import ProductForm, VersionForm
from main.models import Category, Product, Version


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    # def get_queryset(self):
    #     return super().get_queryset().filter(
    #         category=self.kwargs.get('pk')
    #     )

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     category_item = Category.objects.get(pk=self.kwargs.get('pk'))
    #     context_data['category_id'] = category_item.pk
    #     context_data['title'] = f'Продукты из выбранной категории {category_item.name}'
    #     return context_data
    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     category_item = Category.objects.get(pk=self.kwargs.get('pk'))
    #     context_data['category'] = category_item.category
    #     context_data['title'] = f'Продукты из выбранной категории {category_item.name}'
    #     return context_data

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.owner != self.request.user:
    #         raise Http404
    #     return self.object

    @staticmethod
    def all_version():
        return Version.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(
            owner=self.request.user
        )


class ProductCategoryListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category=self.kwargs.get('pk'),
                                   owner=self.request.user)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Продукты из выбранной категории {products_item.name}'
        return context_data


class ProductCardListView(LoginRequiredMixin, ListView):
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


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    permission_required = 'main.add_product'
    form_class = ProductForm
    success_url = reverse_lazy('main:product')


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'main.change_product'
    success_url = reverse_lazy('main:product')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404

        return self.object

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
