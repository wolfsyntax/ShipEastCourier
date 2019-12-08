from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import HomeView, AboutView, ContactView, FAQView, ServiceView, TrackParcelView

urlpatterns = [
    url(r'^about$', AboutView.as_view(), name="about"),
    url(r'^contact$', ContactView.as_view(), name="contact"),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^how-it-works$', FAQView.as_view(), name="guide"),
    url(r'^service$', ServiceView.as_view(), name="services"),
    url(r'^track$', TrackParcelView.as_view(), name="track_parcel"),
	url(r'^track/(?P<tracking_code>[a-zA-Z0-9\-]+)$', TrackParcelView.as_view(), name="trackcode_parcel"),

]
