from django.test import TestCase
from django.urls import reverse

class TestHomePageMessage (TestCase):

    def test_app_title_message_shown_on_home_page(self): 
        url = reverse('home')
        response = self.client.get(url)
        self.assertContains (response, 'Music Videos')

class TestAddVideos (TestCase):
    pass

class TestVideoList(TestCase):
    pass

class TestVideoSearch (TestCase):
    pass

class TestVideoModel (TestCase):
    pass