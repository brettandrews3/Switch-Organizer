from django.contrib import admin

from .models import VideoGame, Review, UserForm

# Register your models here.

class ReviewInline(admin.TabularInline):
	model = Review
	#extra = 1

class VideoGameAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['game_name', 'genre', 'developer', 'publisher',
			'game_console']}),
		('Date information', {'fields': ['release_date', 'pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ReviewInline]

	list_display = ('game_name', 'genre', 'developer', 'release_date')
	search_fields = ['game_name', 'release_date', 'genre', 'developer', 'game_console']
	#list_filter = ['release_date']

admin.site.register(VideoGame, VideoGameAdmin)