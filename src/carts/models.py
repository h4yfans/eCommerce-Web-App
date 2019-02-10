from decimal import Decimal
from django.db import models
from django.conf import settings
from django.db.models import Sum
from django.db.models.signals import pre_save, post_save, m2m_changed
from products.models import Product


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id)
        # if qs.count() == 1:
        if qs.exists() == 1:
            new_obj = False
            print('Cart ID exists')
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            print('Card not exists')
            cart_obj = self.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Product, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamps = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        total = instance.products.aggregate(sumOfProducts=Sum('price'))
        if instance.subtotal != total.get('sumOfProducts'):
            instance.subtotal = total.get('sumOfProducts')
            instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    # Tax, Shipping etc.
    if instance.subtotal > 0:
        instance.total = Decimal(instance.subtotal) * Decimal(1.18)  # %18 tax
    else:
        instance.total = 0.00


pre_save.connect(pre_save_cart_receiver, sender=Cart)
