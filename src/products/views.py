from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from carts.models import Cart

from .models import Product


class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    template_name = 'products/featured-detail.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()


class ProductListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     product = Product.objects.filter(pk=pk)
    #     return product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data()
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found...")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.filter()
        except:
            raise Http404('Uhhmm ')
        return instance


class ProductDetailView(DetailView):
    template_name = 'products/detail.html'

    # def get_object(self, queryset=None):
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("Product doesn't exist")
    #     return instance

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        product = Product.objects.filter(pk=pk)
        return product
