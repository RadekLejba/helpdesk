from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from consultant.models import Category
from client.models import Ticket, STATUS_CHOICES
from helpdesk.views import BaseView


class CreateCategoryView(BaseView, CreateView):
    model = Category
    success_url = 'create_category'
    fields = ['name']
    template_name = 'consultant/create_category.html'


class TicketListView(BaseView, ListView):
    model = Ticket
    template_name = 'consultant/ticket_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tickets = context['ticket_list']

        context['todo_tickets'] = tickets.filter(
            status=STATUS_CHOICES[0][1]
        ).order_by('priority')
        context['in_progres_tickets'] = tickets.filter(
            status=STATUS_CHOICES[1][1]
        ).order_by('priority')
        context['done_tickets'] = tickets.filter(
            status=STATUS_CHOICES[2][1]
        ).order_by('priority')

        return context


class TicketListByCategoryView(BaseView, ListView):
    model = Ticket
    template_name = 'consultant/ticket_list_by_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        tickets = context['ticket_list']
        context['categories'] = {}
        for category in categories:
            context['categories'][category.name] = [
                ticket for ticket in tickets if
                ticket.category == category
            ]

        return context
