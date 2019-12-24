from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView

from .views import HomeView, AboutView, ContactView, FAQView, ServiceView, TrackParcelView

urlpatterns = [
    url(r'^about$', AboutView.as_view(), name="about"),
    url(r'^contact$', ContactView.as_view(), name="contact"),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^how-it-works$', FAQView.as_view(), name="guide"),
    url(r'^service$', ServiceView.as_view(), name="services"),
    url(r'^track$', TrackParcelView.as_view(), name="track_parcel"),
	url(r'^track/(?P<tracking_code>[a-zA-Z0-9\-]+)$', TrackParcelView.as_view(), name="trackcode_parcel"),
	url(r'^rates/$',TemplateView.as_view(template_name="sitemap/rates.html"),{'n':range(1,13), 'part1':[4, 7, 9.5, 12.5, 14.5, 24.5, 26.5, 28.5, 30.5, 32.5, 34.5, 36.5],'part2':[38.5, 40.5, 42.5, 46.5, 48.5, 51.5, 54.5, 57.5, 60.5, 63.5,66.5, 69.5]}, name="rates"),
]
