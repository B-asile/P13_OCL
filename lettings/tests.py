from django.test import TestCase

from faker import Faker
from django.urls import reverse

from .models import Address, Letting


class LettingsTest(TestCase):
    faker = Faker()

    def setUp(self):
        self.address = Address.objects.create(
            number=self.faker.random_int(min=1, max=9999),
            street=self.faker.street_name(),
            city=self.faker.city(),
            state=self.faker.state(),
            zip_code=self.faker.zipcode(),
            country_iso_code=self.faker.country_code(),
        )

        self.letting = Letting.objects.create(
            title='SampleAddress',
            address=self.address,
        )

    def test_index(self):
        response = self.client.get(reverse('lettings:index'))
        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content

    def test_letting(self):
        response = self.client.get(reverse('lettings:letting', args=[self.letting.pk]))
        assert response.status_code == 200
