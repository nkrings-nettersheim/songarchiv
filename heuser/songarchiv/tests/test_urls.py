from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import index, impressum, datenschutz, add_song, search_song, edit_song, song, del_song, song_delete_done
from ..views import autocomplete
from ..views import add_album, search_album_start, search_album, edit_album, album, single
from ..views import add_text, edit_text, text, print_text, print_chordpro, print_chords, print_nashville

class TestUrls(SimpleTestCase):

    def test_url_index_is_resolved(self):
        url = reverse('songarchiv:index')
        self.assertEqual(resolve(url).func, index)

    def test_url_autocomplete_is_resolved(self):
        url = reverse('songarchiv:autocomplete')
        self.assertEqual(resolve(url).func, autocomplete)

    def test_url_impressum_is_resolved(self):
        url = reverse('songarchiv:impressum')
        self.assertEqual(resolve(url).func, impressum)

    def test_url_datenschutz_is_resolved(self):
        url = reverse('songarchiv:datenschutz')
        self.assertEqual(resolve(url).func, datenschutz)

    def test_url_add_song_is_resolved(self):
        url = reverse('songarchiv:add_song')
        self.assertEqual(resolve(url).func, add_song)

    def test_url_search_song_is_resolved(self):
        url = reverse('songarchiv:search_song')
        self.assertEqual(resolve(url).func, search_song)

    def test_url_edit_song_is_resolved(self):
        url = reverse('songarchiv:edit_song', args=['1'])
        self.assertEqual(resolve(url).func, edit_song)

    def test_url_song_is_resolved(self):
        url = reverse('songarchiv:song', args=['1'])
        self.assertEqual(resolve(url).func, song)

    def test_url_del_song_is_resolved(self):
        url = reverse('songarchiv:del_song', kwargs={'pk': '1'})
        self.assertEqual(resolve(url).func.view_class, del_song)

    def test_url_song_del_done_is_resolved(self):
        url = reverse('songarchiv:del_song_done')
        self.assertEqual(resolve(url).func, song_delete_done)

    def test_url_add_album_is_resolved(self):
        url = reverse('songarchiv:add_album')
        self.assertEqual(resolve(url).func, add_album)

    def test_url_search_album_start_is_resolved(self):
        url = reverse('songarchiv:search_album_start')
        self.assertEqual(resolve(url).func, search_album_start)

    def test_url_search_album_is_resolved(self):
        url = reverse('songarchiv:search_album')
        self.assertEqual(resolve(url).func, search_album)

    def test_url_edit_album_is_resolved(self):
        url = reverse('songarchiv:edit_album', args=['1'])
        self.assertEqual(resolve(url).func, edit_album)

    def test_url_album_is_resolved(self):
        url = reverse('songarchiv:album')
        self.assertEqual(resolve(url).func, album)

    def test_url_single_is_resolved(self):
        url = reverse('songarchiv:single')
        self.assertEqual(resolve(url).func, single)

    def test_url_add_text_is_resolved(self):
        url = reverse('songarchiv:add_text')
        self.assertEqual(resolve(url).func, add_text)

    def test_url_edit_text_is_resolved(self):
        url = reverse('songarchiv:edit_text', args=['1'])
        self.assertEqual(resolve(url).func, edit_text)

    def test_url_text_is_resolved(self):
        url = reverse('songarchiv:text', args=['1'])
        self.assertEqual(resolve(url).func, text)

    def test_url_print_text_is_resolved(self):
        url = reverse('songarchiv:print_text')
        self.assertEqual(resolve(url).func, print_text)

    def test_url_print_chordpro_is_resolved(self):
        url = reverse('songarchiv:print_chordpro')
        self.assertEqual(resolve(url).func, print_chordpro)

    def test_url_print_chords_is_resolved(self):
        url = reverse('songarchiv:print_chords')
        self.assertEqual(resolve(url).func, print_chords)

    def test_url_print_nashville_is_resolved(self):
        url = reverse('songarchiv:print_nashville')
        self.assertEqual(resolve(url).func, print_nashville)
