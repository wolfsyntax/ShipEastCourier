from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import RegisterView

urlpatterns = [
	url(r'^join$', RegisterView.as_view(), name="signup"),
]