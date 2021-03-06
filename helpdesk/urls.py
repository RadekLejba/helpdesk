"""helpdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin

from helpdesk.views import IndexRedirectView, SignupView

urlpatterns = [
    path(r'', IndexRedirectView.as_view(), name='index'),
    path(r'', include('django.contrib.auth.urls')),
    path(r'signup/', SignupView.as_view(), name='signup'),
    path(r'client/', include('client.urls')),
    path(r'consultant/', include('consultant.urls')),
    path(r'admin/', admin.site.urls),
]
