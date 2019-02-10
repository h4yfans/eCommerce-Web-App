from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # customer_id Stripe or Braintree
    def __str__(self):
        return self.email


# def billing_profile_created_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         print('ACTUAL API REQUEST send to stripe/braintree')
#         instance.customer_id = newID
#         instance.save()

def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)


post_save.connect(user_created_receiver, sender=User)
