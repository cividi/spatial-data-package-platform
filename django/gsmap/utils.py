from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model


def get_user_from_sessionid(sessionid):
    """
    ``sessionid`` - is the identifier for the users session. 
    You can also find it in the Http500 error messages on screen
    or via email.

    >>> get_user_from_sessionid('fd3479022d77794897e5b23f4d461bbf')
    """

    session = Session.objects.get(session_key=sessionid)
    uid = session.get_decoded().get('_auth_user_id')
    user = get_user_model().objects.get(pk=uid)

    return user