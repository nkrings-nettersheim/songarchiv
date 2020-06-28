from django.contrib import admin

# Register your models here.
from .models import Song, Song_Text, Album

admin.site.register(Song)
admin.site.register(Song_Text)
admin.site.register(Album)
