import os

from django.db import models
from ckeditor.fields import RichTextField


def dynamik_path(instance, filename):
    file_path = '{filename}'.format(filename=filename)
    return file_path


class Song(models.Model):
    song_title = models.CharField(max_length=250)
    song_artist = models.CharField(max_length=250)
    song_music = models.CharField(max_length=250, blank=True, default='')
    song_lyrics = models.CharField(max_length=250, blank=True, default='')
    song_year = models.DateField(blank=True, default='1900-01-01')
    song_publisher = models.CharField(max_length=250, blank=True, default='')
    song_producer = models.CharField(max_length=125, blank=True, default='')
    song_spotify = models.URLField(max_length=250, blank=True, default='')
    song_amazon = models.URLField(max_length=250, blank=True, default='')
    song_itunes = models.URLField(max_length=250, blank=True, default='')
    song_snippet = models.FileField(upload_to=dynamik_path, max_length=100, blank=True)
    song_background = models.TextField(blank=True, default='')

    def __str__(self):
        return self.song_title


class Album(models.Model):
    album_title = models.CharField(max_length=250)
    album_year = models.DateField(default='1900-01-01')

    def __str__(self):
        return self.album_title


class Song_Text(models.Model):
    text_text = RichTextField()
    text_chords = RichTextField()
    text_nashville = RichTextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE, default='')
