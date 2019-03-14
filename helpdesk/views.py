from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView


class BaseView(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class IndexView(BaseView, TemplateView):
    template_name = 'helpdesk/main.html'


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
