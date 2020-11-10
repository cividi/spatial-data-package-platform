from rest_framework import serializers
from .models import Snapshot
from .utils import get_user_from_sessionid


class SnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snapshot
        fields = (
            'id', 'title', 'topic',
        )
        read_only_fields = ('id',)

    def create(self, validated_data):
        request = self.context.get("request")
        cookies = request.COOKIES
        sessionid = cookies.get('sessionid', None)
        if sessionid:
            user = get_user_from_sessionid(sessionid)
        instance = Snapshot.objects.create(user=user, **validated_data)
        return instance