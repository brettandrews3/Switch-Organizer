from django.contrib import admin
from django.urls import path
from . import views

# Adding custom site header, title, index title to the app:
admin.site.site_header = "Video Game Organizer"
admin.site.site_title = "Game Organizer"
admin.site.index_title = "Add games. Get organized." 

# urlpatterns simplifies the web address system for the app

app_name = 'organizer'

urlpatterns = [
	# custom admin site to load the site titles, header defined above:
	path('admin/', admin.site.urls),
	# ex: /organizer/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /organizer/3/
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# ex: /organizer/3/results/
	path('<int:pk>/results', views.ResultsView.as_view, name='results'),
	# ex: /organizer/3/rate/
	path('<int:pk>/rate/', views.rate, name='rate')
]

"""
Existing pattern before 12/30/2021 changes
urlpatterns = [
	# ex: /organizer/
	path('', views.index, name='index'),
	# ex: /organizer/3/
	path('<int:game_id>/', views.detail, name='detail'),
	# ex: /organizer/3/results/
	path('<int:game_id>/results', views.results, name='results')
	# ex: /organizer/3/rating/
	path('<int:game_id>/rating', views.rating, name='rating'),
]
"""