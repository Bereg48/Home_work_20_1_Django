from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import ProductCardListView, ProductListView, CategoryListView, ProductCategoryListView, \
    ProductCreateView, ProductUpdateView, toggle_activity

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(60)(ProductListView.as_view()), name='product'),
    path('category/', cache_page(60)(CategoryListView.as_view()), name='category'),
    path('<int:pk>/main/products_categories/', ProductCategoryListView.as_view(), name='products_categories'),
    path('<int:pk>/main/product_card/', cache_page(10)(ProductCardListView.as_view()), name='product_card'),
    path('create/', ProductCreateView.as_view(), name='create_products'),
    path('<int:pk>/main/update/', ProductUpdateView.as_view(), name='update_products'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),

]
