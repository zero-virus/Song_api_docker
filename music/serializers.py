from rest_framework import serializers
from .models import Songs
from rest_framework.validators import UniqueTogetherValidator


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Songs
        fields = ("title","artist")

        def update(self, instance, validated_data):
            instance.title = validated_data.get("title", instance.title)
            instance.artist = validated_data.get("artist", instance.artist)
            instance.save()
            return instance

        
        validators = [
        UniqueTogetherValidator(
            queryset=Songs.objects.all(),
            fields=('title', 'artist')
        )
    ]
