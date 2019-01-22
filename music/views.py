from django.shortcuts import render
from rest_framework import generics
from .models import Songs
from .serializers import SongSerializer

from rest_framework.response import Response
from rest_framework.views import status

from .decorators import validate_request_data

class ListCreateSongsView(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_song = Songs.objects.create(
            title = request.data["title"],
            artist = request.data["artist"]
        )
        return Response(
            data = SongSerializer(a_song).data,
            status = status.HTTP_201_CREATED
        )

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

    
# Create your views here
