from django.urls import path

from main.apps import MainConfig
from main.views import category, product, products_categories, product_card

app_name = MainConfig.name

urlpatterns = [
    path('', product, name='product'),
    path('category/', category, name='category'),
    path('<int:pk>/main/', products_categories, name='products_categories'),
    path('<str:name>/main/', product_card, name='product_card')

]
