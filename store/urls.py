from django.urls import path
from store.views import home, product_detail, product_list

app_name = 'store'

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
]