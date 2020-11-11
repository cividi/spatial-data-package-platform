from rest_framework import serializers
from .models import Snapshot
from .utils import get_user_from_sessionid


class SnapshotDataUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snapshot
        fields = (
            'data_file',
        )
