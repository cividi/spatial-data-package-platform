import os.path
from django.conf import settings
from django.contrib.sites.models import Site
from sorl.thumbnail.base import ThumbnailBackend, EXTENSIONS
from sorl.thumbnail.conf import settings
from sorl.thumbnail.helpers import tokey, serialize

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
