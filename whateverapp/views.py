from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import City
from .models import Hotel


def index(request):  
    return HttpResponse("Hello world!")


def hotels(request):
    cities_list = City.objects.order_by('name')
    hotels_list = Hotel.objects.order_by('name')
    template = loader.get_template('whateverapp/hotels.html')
    context = RequestContext(request, {
        'cities_list': cities_list,
        'hotels_list': hotels_list
    })
    return HttpResponse(template.render(context))