from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductFeaturedDetailView,
    ProductFeaturedListView,
    ProductDetailSlugView
)

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('featured/', ProductFeaturedListView.as_view(), name='product_featured_list'),
    path('<slug>/', ProductDetailSlugView.as_view(), name='product_slug_detail'),
    path('featured/<pk>/', ProductFeaturedDetailView.as_view(), name='product_featured_detail'),
    path('<pk>/', ProductDetailView.as_view(), name='product_detail'),
]
