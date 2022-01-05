import datetime

from django import forms
from django.contrib import admin
from django.db import models
from django.utils import timezone

rating_numbers=[tuple([x,x]) for x in range(1,11)]

# Create your models here.
class UserForm(forms.Form):
	rating_number = forms.IntegerField(label="How would you rate this game (1-10)?",
		widget=forms.Select(choices=rating_numbers))

class VideoGame(models.Model):
	"""
	This class allows the user to enter the standard data for their
	video games. It starts with the basics: name, release date, publisher,
	genre, console. Other fields may be added later on or appear in child classes. 
	The __str__(self) will be used throughout Django's admin section.
	"""
	game_name = models.CharField(max_length=200)
	release_date = models.CharField(max_length=10, default='yyyy')
	pub_date = models.DateTimeField('date added to organizer', default=timezone.now)
	developer = models.CharField(max_length=50, default='NULL')
	publisher = models.CharField(max_length=50, default='NULL')
	genre = models.CharField(max_length=200)
	game_console = models.CharField(max_length=50, default="Switch")
	def __str__(self):
		return self.game_name
	@admin.display(
		boolean=True,
		ordering='game_name',
		description='Published recently?',
		)
	def was_published_recently(self):
		#return self.pub_date >= timezone.now() - datetime.timedelta(days=1) [BUGGY CODE]
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	

class Review(models.Model):
	"""
	This class will allow for reviews and ratings. Users will be able to save their 
	thoughts on the game and rate the game on a scale of 1-10. The var game holds the
	ForeignKey and links Review class to VideoGame class. review_text generates the text
	box for users to write brief reviews of the games. Finally, rating will allow for
	a numerical score of 1-10 for the game being reviewed. The __str__(self) will be used
	throughout Django's admin section.
	"""
	game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)
	review_text = models.CharField(max_length=1000)
	rating = models.IntegerField(default=1)
	def rating(self):
		userForm = UserForm()
		return userForm.rating_number()
	def __str__(self):
		return self.review_text

"""
Here's where I'm going to draft my drop-down lists for use in genre, game_console,
and rating. For the sake of order, I'm going to try putting the lists down here first
so that I don't have to stack them above the classes. I'll move the lists to the top
of the file if I need to.
"""

