
from django.db import models
from ckeditor.fields import RichTextField


def dynamik_path(instance, filename):
    file_path = '{filename}'.format(filename=filename)
    return file_path


class Album(models.Model):

    ALBUM_SINGLE = (
        ('1', 'Album'),
        ('2', 'Single'),
        ('2', 'LDÖS'),
        ('2', 'Sonstiges'),
    )

    album_title = models.CharField(max_length=250)
    album_year = models.DateField(default='1900-01-01')
    album_cover = models.CharField(max_length=250, default='')
    album_spotify = models.CharField(max_length=500, default='')
    album_amazon_selling = models.CharField(max_length=1000, default='')
    album_single = models.CharField(max_length=20, choices=ALBUM_SINGLE, default='1')

    def __str__(self):
        return self.album_title


class Song(models.Model):
    song_title = models.CharField(max_length=250, unique=True)
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
    song_cover = models.CharField(max_length=125, blank=True, default='')
    song_youtube = models.CharField(max_length=500, blank=True, default='')
    song_amazon_sale = models.CharField(max_length=250, blank=True, default='')
    song_background = models.TextField(blank=True, default='')
    song_activ = models.BooleanField(default=True)
    album = models.ForeignKey(Album, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.song_title

    class Meta:
        ordering = ['album__album_title']


class Song_Text(models.Model):
    text_text = RichTextField()
    text_standard_german = RichTextField()
    text_chordpro = RichTextField()
    text_chords = RichTextField()
    text_nashville = RichTextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.song


class Content_text(models.Model):
    content_kurz = models.CharField(max_length=256, default='')
    content_lang = RichTextField()

    def __str__(self):
        return self.content_kurz

