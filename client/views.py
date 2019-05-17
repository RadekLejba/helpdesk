from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from client.forms import TicketForm
from client.models import Ticket
from helpdesk.views import BaseView


class CreateTicketView(BaseView, CreateView):
    template_name = 'client/create_ticket.html'
    form_class = TicketForm
    success_url = reverse_lazy('create_ticket')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TicketDetailView(BaseView, DetailView):
    model = Ticket


class EditTicketView(BaseView, UpdateView):
    model = Ticket
    template_name = 'client/edit_ticket.html'
    success_url = reverse_lazy('index')
    fields = ['status', 'category', 'priority']

    def get_context_data(self):
        context = super().get_context_data()
        context['pk'] = self.kwargs.get('pk')
        return context


class UserTicketsList(BaseView, ListView):
    model = Ticket
    template_name = 'client/ticket_list.html'

    def get_queryset(self):
        return Ticket.objects.filter(author=self.request.user)
