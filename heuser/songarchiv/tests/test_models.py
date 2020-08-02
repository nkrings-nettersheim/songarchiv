from django.test import TestCase
from ..models import Album


class ModelsTestCase(TestCase):
    def setUp(self):
        self.item = Album()
        self.item.album_title = 'Album Titel'
        self.item.album_year = '1965-05-21'
        self.item.cover = 'cover.png'
        self.item.album_spotify = 'https://www.spotify.com'
        self.item.album_amazon_selling = 'http://www.amazon.de'
        self.item.save()


    def test_album_fields(self):

        record = Album.objects.get(pk=1)
        self.assertEqual(record, self.item)




