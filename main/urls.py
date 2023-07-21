from django.urls import path

from main.apps import MainConfig
from main.views import category, product, products

app_name = MainConfig.name

urlpatterns = [
    path('', category, name='category'),
    path('product/', product, name='product'),
    path('<int:pk>/main/', products, name='products')

]
