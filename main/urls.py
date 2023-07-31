from django.urls import path

from main.apps import MainConfig
from main.views import ProductCardListView, ProductListView, CategoryListView, ProductCategoryListView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('<int:pk>/main/products_categories/', ProductCategoryListView.as_view(), name='products_categories'),
    path('<int:pk>/main/product_card/', ProductCardListView.as_view(), name='product_card')

]
