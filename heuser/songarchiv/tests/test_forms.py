import os
import datetime

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from ..forms import IndexForm, SongTextForm, AlbumForm
from ..models import Song, Song_Text, Album


TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(TEST_DIR, '')

class IndexFormTest(TestCase):
    def test_title_label(self):
        form = IndexForm()
        self.assertTrue(form.fields['title'].label is None or form.fields['title'].label == 'Titel')

class AlbumFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        test_image_path = os.path.join(TEST_DATA_DIR, 'album_endlich_freitag.jpg')

        with open(test_image_path, 'rb') as f:
           testfile = f.read()

        Album.objects.create(
            album_title='Zick es Jlöck',
            album_single='1',
            album_cover_image=SimpleUploadedFile('test.jpg', testfile),
        )

    def test_valid_from(self):
        album = Album.objects.get(id=1)
        print(album.album_cover_image)
#        data = {
#            'album_title': album.album_title,
#            'album_single': album.album_single
#        }
#        form = AlbumForm(data=data)
#        self.assertTrue(form.is_valid())

class SongTextFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        song = Song.objects.create(
            song_title='Als Panz'
        )
        Song_Text.objects.create(
            text_text='Dies ist der Text',
            text_standard_german='Dies ist der hochdeutsche Text',
            text_chordpro='Dies ist der Chordpro Inhalt',
            text_chords='Dies ist der Chords Inhalt',
            text_nashville='Dies ist der Nashville Inhalt',
            song=song,
        )

    def test_text_text_label(self):
        form = SongTextForm()
        self.assertTrue(form.fields['text_text'].label is None or form.fields['text_text'].label == 'Text')

    def test_valid_form(self):
        st = Song_Text.objects.get(id=1)
        data = {
            'text_text': st.text_text,
            'text_standard_german': st.text_standard_german,
            'song': st.song
        }
        form = SongTextForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        st = Song_Text.objects.get(id=1)
        data = {
            'text_text': st.text_text,
            'text_standard_german': st.text_standard_german
        }
        form = SongTextForm(data=data)
        self.assertFalse(form.is_valid())

