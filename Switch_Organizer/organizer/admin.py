from django.contrib import admin

from .models import VideoGame

# Register your models here.

class VideoGameAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['game_name']}),
		('Date information', {'fields': ['pub_date']}),
	]

admin.site.register(VideoGame, VideoGameAdmin)
#admin.site.register(VideoGame)