import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from ..models import Album

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(TEST_DIR, 'data')

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 301)

    def test_songarchiv_loads_properly(self):
        response = self.client.get('/songarchiv/')
        self.assertEqual(response.status_code, 200)

class AlbumListTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_albums = 1
        number_of_singles = 3

        #for album_id in range(number_of_albums):
        Album.objects.create(
            album_title=f"Album_1",
            album_year=f"2000-01-01",
            album_cover_image=SimpleUploadedFile('album_endlich_freitag.jpg', 'these are the file contents!'),
            album_single='1'
        )
        print("Hallo")
#        for album_id in range(number_of_singles):
#            Album.objects.create(
#                album_title=f"Single_{album_id}",
#                album_year=f"2000-01-01",
#                album_cover_image=f"cover/image{album_id}.jpg",
#                album_single='2'
#            )

    #def test_album_list_exists_at_desired_location(self):
    #    response = self.client.get(('/songarchiv/album/'))
    #    self.assertEqual(response.status_code, 200)

    #def test_album_list_accessible_by_name(self):
    #    response = self.client.get(reverse('album'))
    #    self.assertEqual(response.status_code, 200)
