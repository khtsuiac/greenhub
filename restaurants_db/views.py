from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

from .serializers import RestaurantSerializer
from .models import Restaurant

import math

def distance_to_decimal_degrees(distance, latitude):
    """
    Source of formulae information:
        1. https://en.wikipedia.org/wiki/Decimal_degrees
        2. http://www.movable-type.co.uk/scripts/latlong.html
    :param distance: an instance of `from django.contrib.gis.measure.Distance`
    :param latitude: y - coordinate of a point/location
    """
    lat_radians = latitude * (math.pi / 180)
    # 1 longitudinal degree at the equator equal 111,319.5m equiv to 111.32km
    return distance/ (111_319.5 * math.cos(lat_radians))

class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = RestaurantSerializer
    http_method_names = ['get']

    def get_queryset(self):
        query_set = Restaurant.objects.all()
        lat = self.request.query_params.get('lat')
        lng = self.request.query_params.get('lng')
        search = self.request.query_params.get('search')
        dst = self.request.query_params.get('dst')

        if (lat is not None) and (lng is not None) and (dst is not None):
            pnt = Point(float(lng),float(lat),srid=4326)
            query_set = query_set.filter(point__distance_lte=(pnt,distance_to_decimal_degrees(float(dst),float(lat))))
        
        if search is not None:
            query_set = query_set.filter(name__icontains=search)

        return query_set

    


