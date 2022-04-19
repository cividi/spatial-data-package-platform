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
            'state',
            'author_email',
            'usergroup',
            'workspace',
        )
    def validate(self, data):
        if data.get("kind") == 'COM' and not data.get("workspace").annotations_open:
            raise serializers.ValidationError('Adding Comments is currently not allowed for this workspace.')
        if data.get("kind") == 'PLY' and not data.get("workspace").polygon_open:
            raise serializers.ValidationError('Adding Polygons is currently not allowed for this workspace.')
        if data.get("kind") == 'OBJ' and not data.get("workspace").object_open:
            raise serializers.ValidationError('Adding Objects is currently not allowed for this workspace.')
        if not data.get("author_email"):
            raise serializers.ValidationError('Adding annotations to this workspace requires an email.')
        if data.get("workspace").usergroups.all() and not data.get("usergroup"):
            raise serializers.ValidationError('Adding annotations to this workspace requires a usergroup.')
        
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
