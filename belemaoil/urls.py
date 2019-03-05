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


#Authentication
from django.contrib.auth import views as auth_views
from register.forms import LoginForm
from register.views import LandingPageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('register.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^$', auth_views.login, {'template_name': 'index.html','authentication_form': LoginForm}, name="index"),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html','authentication_form': LoginForm}, name='login'),

    url(r'index/$',LandingPageView.as_view(), name='landing'),

    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'), 

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'BELEMAOIL ADMIN DASHBOARD'

