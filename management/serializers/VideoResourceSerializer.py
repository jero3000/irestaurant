from rest_framework import serializers
from management.models import VideoResource


class VideoResourceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='object_id')
    video = serializers.URLField()

    class Meta:
        model = VideoResource
        fields = ('id', 'title', 'pub_date', 'video')
