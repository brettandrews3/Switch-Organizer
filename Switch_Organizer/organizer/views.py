from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import VideoGame

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
			).order_by('name', 'genre')[:5]

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
		"""
		Return HttpResponseRedirect after dealing with the POST data
		successfully. This will prevent data from getting posted twice if
		user hits the Back button on their browser.
		"""
		return HttpResponseRedirect(reverse('reviews:results', args=(game.id,)))