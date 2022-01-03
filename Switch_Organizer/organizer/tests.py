import datetime

from django.test import TestCase
from django.urls import reverse
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

def create_game(game_name, days):
			"""
			Goal: create a game listing with the given 'game_name' and published
			within the given number of 'days' offset to now. In other words, negative
			for games published to the app in the past, positive for games with future
			pub_date.
			"""
			time = timezone.now() + datetime.timedelta(days=days)
			return VideoGame.objects.create(game_name=game_name, pub_date=time)

class VideoGameIndexViewTests(TestCase):   # Changed 'Game' to 'VideoGame', matching the class name.
	def test_no_games(self):
		"""
		If there's no games published, show an appropriate message.
		"""
		#NOTE: THIS RESPONSE ISN'T WORKING ON 1/3/2022***
		response = self.client.get(reverse('organizer:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No games are listed yet. Why not add some?")
		self.assertQuerysetEqual(response.context['latest_games_added'], [])

	def test_past_game(self):
		"""
		Games with a pub_date in the past are shown on the index page.
		"""
		game = create_game(game_name="Past game.", days=-30)
		response = self.client.get(reverse('organizer:index'))
		self.assertQuerysetEqual(
			response.context['latest_games_added'],
			[game],
		)

	def test_future_game(self):
		"""
		Games with a pub_date in the future aren't shown on the index page.
		"""
		create_game(game_name="Future game listing.", days=30)
		response = self.client.get(reverse('organizer:index'))
		self.assertQuerysetEqual(response.context['latest_games_added'], [])

	def test_future_game_and_past_game(self):
		"""
		Only display past games in app, even if both past and future games exist.
		"""
		game = create_game(game_name="Past game.", days=-30)
		create_game(game_name="Future game.", days=30)
		response = self.client.get(reverse('organizer:index'))
		self.assertQuerysetEqual(
			response.context['latest_games_added'],
			[game],
		)

	def test_two_past_questions(self):
		"""
		The games index page can display multiple games.
		"""
		game1 = create_game(game_name="Past game 1.", days=-30)
		game2 = create_game(game_name="Past game 2.", days=-5)
		response = self.client.get(reverse('organizer:index'))
		self.assertQuerysetEqual(
			response.context['latest_games_added'],
			[game2, game1],
		)

class VideoGameDetailViewTests(TestCase):
	def test_future_game(self):
		"""
		The detail view for a game with a future pub_date should return a
		404 not found message for users.
		"""
		future_game = create_game(game_name='Future game.', days=5)
		url = reverse('organizer:detail', args=(future_game.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)

	def test_past_game(self):
		"""
		The detail view for any game with a past pub_date will display the
		game's name.
		"""
		past_game = create_game(game_name='Past game.', days=-5)
		url = reverse('organizer:detail', args=(past_game.id,))
		response = self.client.get(url)
		self.assertContains(response, past_game.game_name)