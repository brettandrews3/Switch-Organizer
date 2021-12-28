from django.urls import path
from . import views

# urlpatterns simplifies the web address system for the app

urlpatterns = [
	# ex: /organizer/
	path('', views.index, name='index'),
	# ex: /organizer/3/
	path('<int:game_id>/', views.detail, name='detail'),
	# ex: /organizer/3/results/
	path('<int:game_id>/', views.results, name='results'),
	# ex: /organizer/3/rating
	path('<int:game_id>/', views.rating, name='rating'),
]