from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

from .serializers import RestaurantSerializer
from .models import Restaurant

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
            pnt = Point(lng,lat,srid =4326)
            query_set = query_set.filter(point__distance_lte=(pnt,float(dst)))
        
        if search is not None:
            query_set = query_set.filter(name__icontains=search)

        return query_set

    


