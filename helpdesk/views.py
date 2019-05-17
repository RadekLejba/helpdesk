from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import RedirectView


class BaseView(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'


class IndexRedirectView(BaseView, RedirectView):
    template_name = 'helpdesk/main.html'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.profile.role == 'Client':
            return 'client/create_ticket'
        else:
            return 'consultant'


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
