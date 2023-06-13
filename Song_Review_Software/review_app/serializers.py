from rest_framework import serializers
from . import models

class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = ['id', 'band', 'title', 'duration']