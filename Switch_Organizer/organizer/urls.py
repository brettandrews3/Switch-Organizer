from django.urls import path
from . import views

# urlpatterns simplifies the web address system for the app
urlpatterns = [
	path('', views.index, name='index'),
]