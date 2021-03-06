from django.urls import path

from client.views import (
    CreateTicketView,
    EditTicketView,
    TicketDetailView,
    UserTicketsList,
)

urlpatterns = [
    path(r'create_ticket/', CreateTicketView.as_view(), name='create_ticket'),
    path(
        r'ticket/<int:pk>',
        TicketDetailView.as_view(),
        name='ticket_details'
    ),
    path(
        r'ticket/<int:pk>/edit',
        EditTicketView.as_view(),
        name='edit_ticket'
    ),
    path(r'user_tickets', UserTicketsList.as_view(), name='user_tickets'),
]
