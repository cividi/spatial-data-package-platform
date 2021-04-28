import pytest

from django.core.management import call_command

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', '/opt/app/fixtures-tests/sites.site.json', verbosity=2)
        call_command('loaddata', '/opt/app/fixtures-tests/gsuser.user.json', verbosity=2)
        call_command('loaddata', '/opt/app/fixtures-tests/gsmap.municipality.json', verbosity=2)
        call_command('loaddata', '/opt/app/fixtures-tests/gsmap.snapshot.json', verbosity=2)
