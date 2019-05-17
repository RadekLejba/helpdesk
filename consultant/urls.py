from django.urls import path

from consultant.views import (
    CreateCategoryView,
    TicketListByCategoryView,
    TicketListView,
)

urlpatterns = [
    path(r'', TicketListView.as_view(), name='ticket_list'),
    path(
        r'ticket_list_by_category',
        TicketListByCategoryView.as_view(),
        name='ticket_list_by_category'
    ),
    path(
        r'create_category', CreateCategoryView.as_view(),
        name='create_category',
    ),
]
