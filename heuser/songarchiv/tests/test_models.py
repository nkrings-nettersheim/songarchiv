from datetime import date

#from django.db.models import ImageFieldFile
from django.db import models
from django.test import TestCase
from ..models import Album, Song, Song_Text, Album_song, Content_text


class AlbumModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Album.objects.create(
            album_title='Zick es Jlöck',
            album_single='1'
        )

    # check if field exists #######################################################################
    def test_it_has_information_fields(self):
        album = Album.objects.get(id=1)
        self.assertIsInstance(album.album_title, str)
        self.assertIsInstance(album.album_spotify, str)
        self.assertIsInstance(album.album_amazon_selling, str)
        self.assertIsInstance(album.album_single, str)
        self.assertIsInstance(album.album_cover_image, models.fields.files.ImageFieldFile)

    def test_it_has_date(self):
        album = Album.objects.get(id=1)
        self.assertIsInstance(album.album_year, date)

    # check label #################################################################################

    def test_album_title_label(self):
        album = Album.objects.get(id=1)
        field_label = album._meta.get_field('album_title').verbose_name
        self.assertEqual(field_label, 'album title')

    def test_album_year_label(self):
        album = Album.objects.get(id=1)
        field_label = album._meta.get_field('album_year').verbose_name
        self.assertEqual(field_label, 'album year')

    def test_album_cover_image_label(self):
        album = Album.objects.get(id=1)
        field_label = album._meta.get_field('album_cover_image').verbose_name
        self.assertEqual(field_label, 'album cover image')

    def test_album_spotify_label(self):
        album = Album.objects.get(id=1)
        field_label = album._meta.get_field('album_spotify').verbose_name
        self.assertEqual(field_label, 'album spotify')

    def test_album_amazon_selling_label(self):
        album = Album.objects.get(id=1)
        field_label = album._meta.get_field('album_amazon_selling').verbose_name
        self.assertEqual(field_label, 'album amazon selling')

    def test_album_single_label(self):
        album = Album.objects.get(id=1)
        field_label = album._meta.get_field('album_single').verbose_name
        self.assertEqual(field_label, 'album single')

    # check max_length ############################################################################
    def test_album_title_max_length(self):
        album = Album.objects.get(id=1)
        max_length = album._meta.get_field('album_title').max_length
        self.assertEqual(max_length, 250)

    def test_album_spotify_max_length(self):
        album = Album.objects.get(id=1)
        max_length = album._meta.get_field('album_spotify').max_length
        self.assertEqual(max_length, 500)

    def test_album_amazon_selling_max_length(self):
        album = Album.objects.get(id=1)
        max_length = album._meta.get_field('album_amazon_selling').max_length
        self.assertEqual(max_length, 1000)

    def test_album_single_max_length(self):
        album = Album.objects.get(id=1)
        max_length = album._meta.get_field('album_single').max_length
        self.assertEqual(max_length, 20)

    # check object_name ############################################################################
    def test_object_name(self):
        album = Album.objects.get(id=1)
        expected_object_name = f'{album.album_title}'
        self.assertEqual(expected_object_name, str(album))


class SongModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        album =Album.objects.create(
            album_title='Zick es Jlöck',
            album_single='1'
        )
        Song.objects.create(
            song_title='Als Panz',
            song_artist='Björn Heuser',
            album=album
        )

    # check if field exists #######################################################################
    def test_it_has_information_fields(self):
        song = Song.objects.get(id=1)
        self.assertIsInstance(song.song_title, str)
        self.assertIsInstance(song.song_tag, str)
        self.assertIsInstance(song.slug, str)
        self.assertIsInstance(song.song_artist, str)
        self.assertIsInstance(song.song_music, str)
        self.assertIsInstance(song.song_lyrics, str)
        self.assertIsInstance(song.song_publisher, str)
        self.assertIsInstance(song.song_producer, str)
        self.assertIsInstance(song.song_spotify_iframe, str)
        self.assertIsInstance(song.song_spotify, str)
        self.assertIsInstance(song.song_amazon, str)
        self.assertIsInstance(song.song_itunes, str)
        self.assertIsInstance(song.song_snippet, models.fields.files.FieldFile)
        self.assertIsInstance(song.song_youtube, str)
        self.assertIsInstance(song.song_youtube_2, str)
        self.assertIsInstance(song.song_youtube_3, str)
        self.assertIsInstance(song.song_amazon_sale, str)
        self.assertIsInstance(song.song_background, str)

    def test_it_has_date(self):
        song = Song.objects.get(id=1)
        self.assertIsInstance(song.song_year, date)

    # check label #################################################################################
    def test_song_title_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_title').verbose_name
        self.assertEqual(field_label, 'song title')

    def test_song_tag_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_tag').verbose_name
        self.assertEqual(field_label, 'song tag')

    def test_song_slug_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_song_artist_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_artist').verbose_name
        self.assertEqual(field_label, 'song artist')

    def test_song_music_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_music').verbose_name
        self.assertEqual(field_label, 'song music')

    def test_song_lyrics_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_lyrics').verbose_name
        self.assertEqual(field_label, 'song lyrics')

    def test_song_year_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_year').verbose_name
        self.assertEqual(field_label, 'song year')

    def test_song_publisher_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_publisher').verbose_name
        self.assertEqual(field_label, 'song publisher')

    def test_song_producer_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_producer').verbose_name
        self.assertEqual(field_label, 'song producer')

    def test_song_spotify_iframe_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_spotify_iframe').verbose_name
        self.assertEqual(field_label, 'song spotify iframe')

    def test_song_spotify_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_spotify').verbose_name
        self.assertEqual(field_label, 'song spotify')

    def test_song_amazon_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_amazon').verbose_name
        self.assertEqual(field_label, 'song amazon')

    def test_song_itunes_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_itunes').verbose_name
        self.assertEqual(field_label, 'song itunes')

    def test_song_snippet_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_snippet').verbose_name
        self.assertEqual(field_label, 'song snippet')

    def test_song_youtube_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_youtube').verbose_name
        self.assertEqual(field_label, 'song youtube')

    def test_song_youtube_2_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_youtube_2').verbose_name
        self.assertEqual(field_label, 'song youtube 2')

    def test_song_youtube_3_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_youtube_3').verbose_name
        self.assertEqual(field_label, 'song youtube 3')

    def test_song_amazon_sale_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_amazon_sale').verbose_name
        self.assertEqual(field_label, 'song amazon sale')

    def test_song_background_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_background').verbose_name
        self.assertEqual(field_label, 'song background')

    def test_song_activ_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('song_activ').verbose_name
        self.assertEqual(field_label, 'song activ')

    def test_album_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('album').verbose_name
        self.assertEqual(field_label, 'album')

    # check max_length ############################################################################
    def test_song_title_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_title').max_length
        self.assertEqual(max_length, 250)

    def test_song_tag_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_tag').max_length
        self.assertEqual(max_length, 500)

    def test_song_slug_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('slug').max_length
        self.assertEqual(max_length, 70)

    def test_song_artist_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_artist').max_length
        self.assertEqual(max_length, 250)

    def test_song_music_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_music').max_length
        self.assertEqual(max_length, 250)

    def test_song_lyrics_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_lyrics').max_length
        self.assertEqual(max_length, 250)

    def test_song_publisher_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_publisher').max_length
        self.assertEqual(max_length, 250)

    def test_song_producer_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_producer').max_length
        self.assertEqual(max_length, 125)

    def test_song_spotify_iframe_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_spotify_iframe').max_length
        self.assertEqual(max_length, 250)

    def test_song_spotify_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_spotify').max_length
        self.assertEqual(max_length, 250)

    def test_song_amazon_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_amazon').max_length
        self.assertEqual(max_length, 250)

    def test_song_itunes_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_itunes').max_length
        self.assertEqual(max_length, 250)

    def test_song_snippet_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_snippet').max_length
        self.assertEqual(max_length, 100)

    def test_song_youtube_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_youtube').max_length
        self.assertEqual(max_length, 500)

    def test_song_youtube_2_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_youtube_2').max_length
        self.assertEqual(max_length, 500)

    def test_song_youtube_3_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_youtube_3').max_length
        self.assertEqual(max_length, 500)

    def test_song_amazon_sale_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('song_amazon_sale').max_length
        self.assertEqual(max_length, 250)

    # check object_name ############################################################################
    def test_object_name(self):
        song = Song.objects.get(id=1)
        expected_object_name = f'{song.song_title}'
        self.assertEqual(expected_object_name, str(song))

    # check get absolute url ############################################################################
    def test_get_absolute_url(self):
        song = Song.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(song.get_absolute_url(), '/songarchiv/song/bjoern-heuser-als-panz/')

    # check foreignkey field ######################################################################
    def test_album_foreign_key_field(self):
        song = Song.objects.get(id=1)
        self.assertEqual(song.album.album_title, "Zick es Jlöck")

class Song_TextModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        song = Song.objects.create(song_title='Als Panz')
        Song_Text.objects.create(
            text_text='Dies ist der Songtext',
            text_standard_german='Dies ist die Übersetzung',
            text_chordpro='Dies ist die Chordpro Version',
            text_chords='Dies ist die Chord Version',
            text_nashville='Dies ist der Nashville Style',
            song=song
        )

    # check if field exists #######################################################################
    def test_it_has_information_fields(self):
        song_text = Song_Text.objects.get(id=1)
        self.assertIsInstance(song_text.text_text, str)
        self.assertIsInstance(song_text.text_standard_german, str)
        self.assertIsInstance(song_text.text_chordpro, str)
        self.assertIsInstance(song_text.text_chords, str)
        self.assertIsInstance(song_text.text_nashville, str)

    # check label #################################################################################
    def test_text_text_label(self):
        song_text = Song_Text.objects.get(id=1)
        field_label = song_text._meta.get_field('text_text').verbose_name
        self.assertEqual(field_label, 'text text')

    def test_slug_label(self):
        song_text = Song_Text.objects.get(id=1)
        field_label = song_text._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_text_standard_german_label(self):
        song_text = Song_Text.objects.get(id=1)
        field_label = song_text._meta.get_field('text_standard_german').verbose_name
        self.assertEqual(field_label, 'text standard german')

    def test_text_chordpro_label(self):
        song_text = Song_Text.objects.get(id=1)
        field_label = song_text._meta.get_field('text_chordpro').verbose_name
        self.assertEqual(field_label, 'text chordpro')

    def test_text_chords_label(self):
        song_text = Song_Text.objects.get(id=1)
        field_label = song_text._meta.get_field('text_chords').verbose_name
        self.assertEqual(field_label, 'text chords')

    def test_text_nashville_label(self):
        song_text = Song_Text.objects.get(id=1)
        field_label = song_text._meta.get_field('text_nashville').verbose_name
        self.assertEqual(field_label, 'text nashville')

    def test_song_label(self):
        song_text = Song_Text.objects.get(id=1)
        field_label = song_text._meta.get_field('song').verbose_name
        self.assertEqual(field_label, 'song')

    # check max_length ############################################################################
    def test_slug_max_length(self):
        song_text = Song_Text.objects.get(id=1)
        max_length = song_text._meta.get_field('slug').max_length
        self.assertEqual(max_length, 70)

    # check object_name ###########################################################################
    def test_object_name(self):
        song_text = Song_Text.objects.get(id=1)
        expected_object_name = f'{song_text.song.song_title}'
        self.assertEqual(expected_object_name, str(song_text))

    # check get absolute url ######################################################################
    def test_get_absolute_url(self):
        song_text = Song_Text.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(song_text.get_absolute_url(), '/songarchiv/text/bjoern-heuser-als-panz/')

    # check foreignkey field ######################################################################
    def test_song_foreign_key_field(self):
        song_text = Song_Text.objects.get(id=1)
        self.assertEqual(song_text.song.song_title, "Als Panz")


class Album_songModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        song = Song.objects.create(song_title='Als Panz')
        album = Album.objects.create(album_title='Zick es Jlöck')
        Album_song.objects.create(
            album=album,
            song=song,
            position=1
        )

    # check if field exists #######################################################################
    def test_it_has_information_fields(self):
        album_song = Album_song.objects.get(id=1)
        self.assertIsInstance(album_song.position, int)

    # check label #################################################################################
    def test_album_label(self):
        album_song = Album_song.objects.get(id=1)
        field_label = album_song._meta.get_field('album').verbose_name
        self.assertEqual(field_label, 'album')

    def test_song_label(self):
        album_song = Album_song.objects.get(id=1)
        field_label = album_song._meta.get_field('song').verbose_name
        self.assertEqual(field_label, 'song')

    def test_position_label(self):
        album_song = Album_song.objects.get(id=1)
        field_label = album_song._meta.get_field('position').verbose_name
        self.assertEqual(field_label, 'position')

    # check object_name ############################################################################
    def test_object_name(self):
        album_song = Album_song.objects.get(id=1)
        expected_object_name = ("%s %s %s %s" % (album_song.album.album_title, album_song.song.song_title, album_song.song.id, album_song.position))
        self.assertEqual(expected_object_name, str(album_song))


class Content_textModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.content_text = Content_text.objects.create(
            content_kurz='Dies ist der Kurztext',
            content_lang='Dies ist der Langtext'
        )
    # check if field exists #######################################################################
    def test_it_has_information_fields(self):
        content_text = Content_text.objects.get(id=1)
        self.assertIsInstance(content_text.content_kurz, str)
        self.assertIsInstance(content_text.content_lang, str)

    # check label #################################################################################
    def test_content_kurz_label(self):
        content_text = Content_text.objects.get(id=1)
        field_label = content_text._meta.get_field('content_kurz').verbose_name
        self.assertEqual(field_label, 'content kurz')

    def test_content_lang_label(self):
        content_text = Content_text.objects.get(id=1)
        field_label = content_text._meta.get_field('content_lang').verbose_name
        self.assertEqual(field_label, 'content lang')

    # check max_length ############################################################################
    def test_content_kurz_max_length(self):
        content_text = Content_text.objects.get(id=1)
        max_length = content_text._meta.get_field('content_kurz').max_length
        self.assertEqual(max_length, 256)

    # check object_name ############################################################################
    def test_object_name(self):
        content_text = Content_text.objects.get(id=1)
        expected_object_name = f'{content_text.content_kurz}'
        self.assertEqual(expected_object_name, str(content_text))
