from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic

from .models import *
from .forms import VideoGameForm

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'organizer/index.html'
	context_object_name = 'latest_games_added'

	def get_queryset(self):
		"""
		Return the last 5 games I published on the app. Exclude
		any games set to be published to the app in the future.
		"""
		return VideoGame.objects.filter(
			pub_date__lte=timezone.now()
			).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = VideoGame
	template_name = 'organizer/detail.html'

	def get_queryset(self):
		"""
		Exclude any games that aren't published to the app yet.
		"""
		return VideoGame.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = VideoGame
	template_name = 'organizer/results.html'

class VideoGameCreateView(generic.CreateView):
	model = VideoGame
	form_class = VideoGameForm
	success_url = reverse_lazy('game_changelist')

class VideoGameUpdateView(generic.UpdateView):
	model = VideoGame
	form_class = VideoGameForm
	success_url = reverse_lazy('game_changelist')

"""
def index(request):
	latest_games_added = VideoGame.objects.order_by('-pub_date')[:5]
	template = loader.get_template('organizer/index.html')
	context = {'latest_games_added': latest_games_added}
	return render(request, 'organizer/index.html', context)
	#return HttpResponse(template.render(context, request))
	#output = ', '.join([v.game_name for v in latest_games_added])
	#return HttpResponse(output)
	#return HttpResponse("Hello, friendo. You're at the organizer index.")


# Here's the standardized HttpResponses for urlpatterns in urls.py:
def detail(request, game_id):
	game = get_object_or_404(VideoGame, pk=game_id)
	return render(request, 'organizer/detail.html', {'game': game})

def results(request, game_id):
	game = get_object_or_404(VideoGame, pk=game_id)
	return render(request, 'organizer/results.html', {'game': game})
"""

"""def results(request, game_id):
	response = "You're looking at the results of game %s."
	return HttpResponse(response % game_id)"""

def rating(request, game_id):
	return HttpResponse("You're rating game %s." % game_id)

def rate(request, game_id):
	game = get_object_or_404(VideoGame, pk=game_id)
	try:
		selected_review = game.review_set.get(pk=request.POST['review'])
	except (KeyError, Review.DoesNotExist):
		# Should redisplay the rating form:
		return render(request, 'organizer/detail.html', {
			'game': game,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_review.recommends += 1 # In text recommends = 'votes' here
		selected_review.save()
		"""Return HttpResponseRedirect after dealing with the POST data
		successfully. This will prevent data from getting posted twice if
		user hits the Back button on their browser.
		"""
		return HttpResponseRedirect(reverse('reviews:results', args=(game.id,)))