from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from client.forms import TicketForm
from client.models import Ticket
from helpdesk.views import BaseView


class CreateTicketView(BaseView, CreateView):
    template_name = 'client/create_ticket.html'
    form_class = TicketForm
    success_url = 'create_ticket'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TicketDetailView(DetailView):
    model = Ticket


class EditTicketView(UpdateView):
    model = Ticket
    template_name = 'client/edit_ticket.html'
    success_url = reverse_lazy('index')
    fields = ['status', 'category', 'priority']
