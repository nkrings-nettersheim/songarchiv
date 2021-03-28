
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify

# diese Funktion kann ggf. weg, da sie in songs bei den snipplet eingesetzt war, aber eigentlich nicht benötigt wird
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
    album_cover_image = models.ImageField(upload_to='cover/', null=True, blank=True)
    album_spotify = models.CharField(max_length=500, default='')
    album_amazon_selling = models.CharField(max_length=1000, default='')
    album_single = models.CharField(max_length=20, choices=ALBUM_SINGLE, default='1')

    def __str__(self):
        return self.album_title


class Song(models.Model):
    song_title = models.CharField(max_length=250, unique=True)
    song_tag = models.CharField(max_length=500, blank=True, default="")
    slug = models.SlugField(max_length=70, null=True, blank=True)
    song_artist = models.CharField(max_length=250)
    song_music = models.CharField(max_length=250, blank=True, default='')
    song_lyrics = models.CharField(max_length=250, blank=True, default='')
    song_year = models.DateField(blank=True, default='1900-01-01')
    song_publisher = models.CharField(max_length=250, blank=True, default='')
    song_producer = models.CharField(max_length=125, blank=True, default='')
    song_spotify_iframe = models.CharField(max_length=250, blank=True, default='')
    song_spotify = models.URLField(max_length=250, blank=True, default='')
    song_amazon = models.URLField(max_length=250, blank=True, default='')
    song_itunes = models.URLField(max_length=250, blank=True, default='')
    song_snippet = models.FileField(upload_to='mp3/', max_length=100, blank=True)
    song_youtube = models.CharField(max_length=500, blank=True, default='')
    song_youtube_2 = models.CharField(max_length=500, blank=True, default='')
    song_youtube_3 = models.CharField(max_length=500, blank=True, default='')
    song_amazon_sale = models.CharField(max_length=250, blank=True, default='')
    song_background = models.TextField(blank=True, default='')
    song_activ = models.BooleanField(default=True)
    album = models.ForeignKey(Album, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.song_title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            german_title = self.song_title.lower()
            german_title = (german_title.translate(str.maketrans({'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss'})))
            german_title = 'bjoern-heuser-' + german_title
            self.slug = slugify(german_title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        #return "/songarchiv/song/%s/" % self.slug
        return reverse('songarchiv:song', args=[str(self.slug)])
        #return reverse('songarchiv:song', kwargs={'id': self.id, 'slug': self.slug })


    class Meta:
        ordering = ['album__album_title']


class Song_Text(models.Model):
    text_text = RichTextField()
    slug = models.SlugField(max_length=70, null=True, blank=True)
    text_standard_german = RichTextField()
    text_chordpro = RichTextField()
    text_chords = RichTextField()
    text_nashville = RichTextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.song.song_title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = self.song.slug
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('songarchiv:text', args=[str(self.slug)])


class Content_text(models.Model):
    content_kurz = models.CharField(max_length=256, default='')
    content_lang = RichTextField()

    def __str__(self):
        return self.content_kurz

