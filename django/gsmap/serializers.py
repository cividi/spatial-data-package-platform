from rest_framework import serializers
from .models import Snapshot, Annotation
from .utils import get_user_from_sessionid


class SnapshotDataUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snapshot
        fields = (
            'data_file',
        )

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = (
            'kind',
            'data',
            'category',
            'author_email',
            'rating',
            'workspace',
        )

class AnnotationRateUpSerializer(serializers.ModelSerializer):
    annotations_open = serializers.BooleanField()

    class Meta:
        model = Annotation
        fields = ('rating', 'annotations_open')

    def validate(self, data):
        if not data.get("annotations_open"):
            raise serializers.ValidationError(f'Rating annotations is not allowed currently for this workspace.')
        return data
