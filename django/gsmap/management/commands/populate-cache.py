import os
import json
from gsmap.tasks import update_cache
from gsmap.models import Workspace
from main.settings import LANGUAGES, API_CACHE_ROOT
from django.core.management.base import BaseCommand


class CacheGenerator(object):
    def __init__(self, path):
        self.path = path

    def trigger_cache_update(self):
        workspaces = Workspace.objects.all()
        for workspace in workspaces:
            for lang in LANGUAGES:
                update_cache.delay(workspace.pk, lang[0])

class Command(BaseCommand):
    help = 'Populate inital workspace cache for all workspaces and language versions'

    def handle(self, *args, **options):
        generator = CacheGenerator(API_CACHE_ROOT)
        generator.trigger_cache_update()

