import json
from jsonslicer import JsonSlicer
from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.gis.geos import GEOSGeometry
from gsmap.models import Municipality


class MunicipalityImporter(object):
    def __init__(self, filename):
        self.filename = filename

    def import_features(self, features):
        with transaction.atomic():
            for feature in features:
                polygons3d = feature['geometry']['coordinates']
                polygons2d = []
                for polygon in polygons3d:
                    new_polygon = []
                    for points in polygon:
                        new_points = []
                        for long, lat, _ in points:
                            new_points.append([lat, long])
                        new_polygon.append(new_points)
                    polygons2d.append(new_polygon)
                geojson = {
                    "type": "MultiPolygon",
                    "coordinates": polygons2d
                }
                Municipality.objects.update_or_create(
                    pk=feature['properties']['gemeinde.BFS_NUMMER'],
                    defaults=dict(
                        name=feature['properties']['gemeinde.NAME'],
                        canton=feature['properties']['kanton.KUERZEL'],
                        perimeter=GEOSGeometry(json.dumps(geojson)),
                    )
                )



    def import_file(self):
        with open(self.filename) as json_file:
            features_iterator = JsonSlicer(json_file, ('features', None))
            while True:
                features_100 = []
                try:
                    features_100 = []
                    for _ in range(100):
                        feature = next(features_iterator)
                        features_100.append(feature)
                except StopIteration:
                    self.import_features(features_100)
                    print('.', flush=True)
                    break
                else:
                    self.import_features(features_100)
                    print('.', flush=True, end='')
        json_file.close()


class Command(BaseCommand):
    help = 'import the a geojson municipality file'

    def add_arguments(self, parser):
        parser.add_argument('geojson_file')

    def handle(self, *args, **options):
        importer = MunicipalityImporter(options['geojson_file'])
        importer.import_file()
