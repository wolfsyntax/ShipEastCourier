from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import RegisterView, DashboardView, TestView

urlpatterns = [
	url(r'^join$', RegisterView.as_view(), name="signup"),
	url(r'^dashboard$', DashboardView.as_view(), name="dashboard"),
	url(r'^test2$', TestView.as_view(), name="test2_view"),
]