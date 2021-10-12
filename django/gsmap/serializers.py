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
