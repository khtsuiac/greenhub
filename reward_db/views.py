from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

from .serializers import RewardSerializer
from .models import Reward

import math

class RewardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = RewardSerializer
    http_method_names = ['get','post']
    queryset = Reward.objects.all()


    


