from django.urls import path

from consultant.views import (
    CreateCategoryView,
    TicketListView,
)

urlpatterns = [
    path(r'', TicketListView.as_view(), name='ticket_list'),
    path(
        r'create_category', CreateCategoryView.as_view(),
        name='create_category',
    ),
]
