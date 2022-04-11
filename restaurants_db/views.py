from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RestaurantSerializer
from .models import Restaurant


def index(request):
    return HttpResponse("Hello, world. You're at the restaurant DB index.")

@api_view(['GET', 'POST'])

def get_all(request):
    if request.method == 'GET':
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

