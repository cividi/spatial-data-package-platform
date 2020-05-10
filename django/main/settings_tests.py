from .settings import *

SECRET_KEY = "#7r1uf5su86d($ita6venjygkru5zfe0)bkj68x0e8*)w6nar6"
DEBUG = True
USE_HTTPS = False

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'webui-tests    ',
        'USER': os.getenv('DJANGO_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
        'HOST': os.getenv('DJANGO_DB_HOST', 'pdb'),
        'PORT': '5432',
        'CONN_MAX_AGE': 600,
        # 'OPTIONS': {'autocommit': True}
    }
}

SAVE_SCREENSHOT_ENABLED = False
