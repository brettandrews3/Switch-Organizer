from django import forms
from .models import *

# Adapted from 'How to implement dependent/chained dropdown list with Django'

class VideoGameForm(forms.ModelForm):
	class Meta:
		model = VideoGame
		fields = ('game_name', 'genre', 'developer', 'publisher', 'game_console')
		""""
		fieldsets = [
		(None, {'fields': ['game_name', 'genre', 'developer', 'publisher',
			'game_console']}),
		('Date information', {'fields': ['release_date', 'pub_date'], 'classes': ['collapse']}),
		]
		"""

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['genre'].queryset = VideoGame.objects.none()