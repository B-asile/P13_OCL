from django.test import TestCase
from django.urls import reverse


def test_dummy():
    assert 1


class OcLettingsSiteTest(TestCase):

    def test_index(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == 200
        assert b"<title>Holiday Homes</title>" in response.content
