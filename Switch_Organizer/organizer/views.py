from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import VideoGame

# Create your views here.

def index(request):
	"""This function creates the index for the organizer app.
	"""
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
	response = "You're looking at the results of game %s."
	return HttpResponse(response % game_id)

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