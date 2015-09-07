from django.test import TestCase
from whateverapp.models import *
import factory


class CityFactory(factory.DjangoModelFactory):
    class Meta:
        model = City

    name = "New York City"


class HotelFactory(factory.DjangoModelFactory):
    class Meta:
        model = Hotel

    name = "Omni",
    room_charge = 489.00
    rooms_available = True,
    rating = "5 Star"
    city = factory.SubFactory(CityFactory)


class HotelTestCase(TestCase):

    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_get_rating(self):
        city = CityFactory.create()
        hotel = HotelFactory.create()
        self.assertEqual(hotel.rating, "5 Star")
        self.assertEqual(hotel.city.name, city.name)
