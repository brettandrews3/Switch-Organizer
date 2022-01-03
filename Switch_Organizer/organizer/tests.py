import datetime

from django.test import TestCase
from django.test import SimpleTestCase
from django.utils import timezone

from .models import VideoGame

# Create your tests here.

class GameModelTests(TestCase):
	def test_was_published_recently_with_future_game(self):
		"""
		Goal: was_published_recently() will return False for games
		with pub_dates in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_game = VideoGame(pub_date=time)
		self.assertIs(future_game.was_published_recently(), False)

	def test_was_published_recently_with_old_game(self):
		"""
		Goal: was_published_recently() will return False for games
		with pub_date older than 1 day.
		"""
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_game = VideoGame(pub_date=time)
		self.assertIs(old_game.was_published_recently(), False)

	def test_was_published_recently_with_recent_game(self):
		"""
		Goal: was_published_recently() will return True for games
		with pub_date within the last 24 hours.
		"""
		time = timezone.now() - datetime.timedelta(hours=23,minutes=59, seconds=59)
		recent_game = VideoGame(pub_date=time)
		self.assertIs(recent_game.was_published_recently(), True)