from django.shortcuts import render
from rest_framework import generics
from .models import Song
from .serializers import SongSerializers
from . import serializers, models


# Create your views here.
class SongList(generics.ListAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializers