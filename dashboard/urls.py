"""belemaoil URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth import views as auth_views
from views import * 


urlpatterns = [

    url(r'login/$',LoginView.as_view(), name='dashboard_login'),
    url(r'logout/$',LogoutView.as_view(), name='dashboard_logout'),
    url(r'informations/$',CInfoView.as_view(), name='dashboard_cinfo'),
    url(r'^$',HomeView.as_view(), name='dashboard_home'),



]

