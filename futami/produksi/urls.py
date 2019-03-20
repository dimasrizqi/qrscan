from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^json$', views.json),
	url(r'^(?P<produksi_id>[0-9]+)$', views.release),
]