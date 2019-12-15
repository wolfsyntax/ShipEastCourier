"""ShipEast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include

from django.conf import settings
from django.conf.urls import url, handler400, handler403, handler404, handler500 

from django.views.generic import TemplateView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include(('sitemap.urls', 'sitemap'))),
    url(r'^',include(('account.urls', 'account'))),
    url(r'^',include('django.contrib.auth.urls')),
    url(r'^test$',TemplateView.as_view(template_name="account/customer/index.html"), name="Test_App"),
]

if not settings.DEBUG:

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]

handler400 = 'sitemap.views.bad_request'
handler403 = 'sitemap.views.permission_denied' 
handler404 = 'sitemap.views.not_found' 
handler500 = 'sitemap.views.server_error' 
