from django.urls import path
from products.views import home_view, product_view, product_form


urlpatterns = [
    path('', home_view, name='home_page'),
    path('products/', product_view, name='product_page'),
    path('add_product/', product_form, name='add_product_page'),
]
