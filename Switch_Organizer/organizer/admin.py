from django.contrib import admin

from .models import VideoGame, Review

# Register your models here.
"""
class ReviewInline(admin.TabularInline):
	model = Review
"""	#extra = 1


"""
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
"""

@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
	list_display = ('game_name', 'genre', 'developer', 'publisher', 'game_console')
	ordering = ('game_name',)
	search_fields = ('game_name', 'game_console', 'release_date', 'genre', 'developer', 'pub_date')
	list_per_page = 500
"""
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	fields = (('game', 'rating'), 'review_text')
	list_display = ('game', 'review_text')
	list_filter = ('-pub_date', 'rating')

class ReviewInline(admin.TabularInline):
	model = Review
	#extra = 1 
"""