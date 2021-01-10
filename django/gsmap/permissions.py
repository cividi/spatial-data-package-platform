from django.contrib.auth import get_user_model

from rest_framework import permissions

from .utils import get_user_from_sessionid


# Permissions
# -----------


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        cookies = request.COOKIES
        sessionid = cookies.get('sessionid', None)
        if sessionid:
            try:
                user = get_user_from_sessionid(sessionid)
                return True
            except:
                return False
        return False