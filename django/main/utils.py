import os.path
from django.conf import settings
from django.contrib.sites.models import Site
from sorl.thumbnail.base import ThumbnailBackend, EXTENSIONS
from sorl.thumbnail.conf import settings
from sorl.thumbnail.helpers import tokey, serialize
import unicodedata


class PermalinkThumbnailBackend(ThumbnailBackend):
    def _get_thumbnail_filename(self, source, geometry_string, options):
        """
        Computes the destination filename.
        """
        key = tokey(source.key, geometry_string, serialize(options))
        filename, _ext = os.path.splitext(os.path.basename(source.name))
        path = '%s/%s' % (key, filename)
        return '%s%s.%s' % (settings.THUMBNAIL_PREFIX, path, EXTENSIONS[options['format']])

def context_processor(request):
    return {
        'ADMIN_HEADER_COLOR': settings.ADMIN_HEADER_COLOR,
        'LOGIN_PAGE_TITLE': settings.LOGIN_PAGE_TITLE,
        'CURRENT_TAG_VERSION': settings.CURRENT_TAG_VERSION,
        'CURRENT_COMMIT_VERSION': settings.CURRENT_COMMIT_VERSION
    }

def get_website(current):
    proto = 'https' if settings.USE_HTTPS else 'http'
    return {'domain': current.domain, 'proto': proto, 'base': f'{proto}://{current.domain}'}

def get_backend():
    proto = 'https' if settings.USE_HTTPS else 'http'
    return {'domain': settings.HOST, 'proto': proto, 'base': f'{proto}://{settings.HOST}'}

def generate_username(email):
    # Using Python 3 and Django 1.11, usernames can contain alphanumeric
    # (ascii and unicode), _, @, +, . and - characters. So we normalize
    # it and slice at 150 characters.
    return unicodedata.normalize('NFKC', email)[:150]


def oidc_op_logout(request):
    oidc_op_logout_endpoint = settings.OIDC_OP_LOGOUT_ENDPOINT
    redirect_url = request.build_absolute_uri(getattr(settings, 'LOGOUT_REDIRECT_URL', '/'))
    return '{}?redirect_uri={}'.format(oidc_op_logout_endpoint, redirect_url)