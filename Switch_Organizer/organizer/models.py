from django.db import models

# Create your models here.
class VideoGame(models.Model):
	"""This class allows the user to enter the standard data for their
	video games. It starts with the basics: name, release date, publisher,
	genre, console. Other fields may be added later on.
	"""
	game_name = models.CharField(max_length=200)
	release_date = models.DateTimeField('date released')
	publisher = models.CharField(max_length=50)
	genre = models.CharField(max_length=200)
	game_console = models.CharField(max_length=50)

class Choice(models.Model):
	"""TODO: This class will allow for reviews and ratings by the time of project
	completion. Users will be able to save their thoughts on the game and rate
	the game on a scale of 1-10. For this initial code draft, I'm using the 
	Django poll tutorial's fields as placeholders while I figure this out.
	"""
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=1000)
	votes = models.IntegerField(default=0)