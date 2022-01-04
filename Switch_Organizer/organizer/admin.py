from django.contrib import admin

from .models import VideoGame, Review

# Register your models here.

class ReviewInline(admin.TabularInline):
	model = Review
	extra = 1

class VideoGameAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['game_name']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ReviewInline]

	list_display = ('game_name', 'genre', 'developer', 'release_date')
	#list_filter = ['release_date']

admin.site.register(VideoGame, VideoGameAdmin)