from django.urls import path
from . import views

urlpatters = [
	path(r'^signup/$', views.signup, name='signup'),
]
