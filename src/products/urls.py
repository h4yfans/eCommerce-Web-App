from django.urls import path
from .views import ProductListView, ProductDetailView

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('<pk>/', ProductDetailView.as_view(), name='product_detail'),
]
