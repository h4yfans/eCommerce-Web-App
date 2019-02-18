from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import UpdateView

from .forms import MarketingPreferenceForm
from .models import MarketingPreference


class MarketingPreferenceUpdateView(SuccessMessageMixin, UpdateView):
    form_class = MarketingPreferenceForm
    template_name = 'base/forms.html'
    success_url = '/settings/email'
    success_message = 'Your email preferences have been updated. Thank you.'
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user:
            return redirect('/login/?next=/settings/email/')
        return super(MarketingPreferenceUpdateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MarketingPreferenceUpdateView, self).get_context_data()
        context['title'] = 'Update Email Preference'
        return context

    def get_object(self, queryset=None):
        user = self.request.user
        obj, created = MarketingPreference.objects.get_or_create(user=user)
        return obj
