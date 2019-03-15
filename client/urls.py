from django.urls import include, path
from django.contrib import admin

from helpdesk.views import IndexView

urlpatterns = [
    path(r'', IndexView.as_view(), name='user_index'),
]
