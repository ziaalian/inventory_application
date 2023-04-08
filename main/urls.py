from django.urls import path
from .views import search_product, product_list, add_product

urlpatterns = [
    path('', search_product, name="search"),
    path('product/', product_list, name='product_list'), # change the URL pattern for product_list view
    path('product/<slug:category_slug>/', product_list, name='product_list_category'),
    path('add/', add_product, name="add"),
]
