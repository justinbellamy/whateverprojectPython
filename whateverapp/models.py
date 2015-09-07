from django.db import models

# Create your models here.
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=64)
    room_charge = models.DecimalField(max_digits=6, decimal_places=2)
    rooms_available = models.BooleanField(default=False)
    rating = models.CharField(choices=(
        ('1', "1 Star"),
        ('2', "2 Stars"),
        ('3', "3 Stars"),
        ('4', "4 Stars"),
        ('5', "5 Stars")),
        max_length=1
    )
    city = models.ForeignKey("City")

    def __unicode__(self):
        return self.name
