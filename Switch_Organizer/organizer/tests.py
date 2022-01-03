import datetime

from django.test import TestCase
from django.test import SimpleTestCase
from django.utils import timezone

from .models import VideoGame

# Create your tests here.

class GameModelTests(TestCase):
	def test_was_published_recently_with_future_game(self):
		"""
		Goal : was_published_recently will return 'False' for games
		with pub_dates in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_game = VideoGame(pub_date=time)
		self.assertIs(future_game.was_published_recently(), False)