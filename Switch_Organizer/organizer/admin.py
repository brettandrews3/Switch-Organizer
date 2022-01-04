from django.contrib import admin

from .models import VideoGame, Review

# Register your models here.

class ReviewInline(admin.TabularInline):
	model = Review
	extra = 3

class VideoGameAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['game_name']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ReviewInline]

admin.site.register(VideoGame, VideoGameAdmin)
#admin.site.register(VideoGame)