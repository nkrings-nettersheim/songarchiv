from django.test import TestCase

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 301)

    def test_songarchiv_loads_properly(self):
        response = self.client.get('/songarchiv/')
        self.assertEqual(response.status_code, 200)
