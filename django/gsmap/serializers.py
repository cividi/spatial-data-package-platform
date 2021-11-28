from rest_framework import serializers
from .models import Snapshot, Annotation


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
            'workspace',
        )
    
    def validate(self, data):
        if not data.get("workspace").annotations_open:
            raise serializers.ValidationError(f'Rating annotations is not allowed currently for this workspace.')
        if not data.get("author_email"):
            raise serializers.ValidationError(f'Adding annotations to this workspace requires an email.')
        
        return data

class AnnotationRateUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ('rating',)
    
    def update(self, instance, validated_data):
        if instance.workspace.annotations_likes_enabled:
            instance.rating = instance.rating + 1
        instance.save()

        return instance
