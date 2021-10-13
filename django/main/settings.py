import os
import os.path

# use your own secret_key, default for testing and dev
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY') or os.getenv('DJANGO_SECRET_KEY_DEV')
DEBUG = os.getenv('DJANGO_DEBUG') == 'True'
USE_HTTPS = os.getenv('DJANGO_HTTPS') == 'True'


if USE_HTTPS:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # SECURE_SSL_REDIRECT = True

EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST', 'maildev')
ADMINS = os.environ.get('DJANGO_ADMINS', 'admin@local.lan').split(',')
ADMINS = list(zip(ADMINS, ADMINS))
MANAGERS = ADMINS
ADMIN_NAME = os.environ.get('DJANGO_ADMIN_NAME', 'dføur DEV')
ADMIN_HEADER_COLOR = os.environ.get('DJANGO_ADMIN_HEADER_COLOR', '#543076')
LOGIN_PAGE_TITLE = os.environ.get('LOGIN_PAGE_TITLE', 'dføur')

CURRENT_TAG_VERSION = "NaN.NaN.NaN"
CURRENT_COMMIT_VERSION = "NaN"

if os.path.isfile("VERSION"):
    with open("VERSION", 'r') as f:
        try:
            content = f.read().split("\t")
            CURRENT_TAG_VERSION = content[0]
            CURRENT_COMMIT_VERSION = content[1]
        except:
            pass

if os.environ.get('DJANGO_ALLOWED_HOSTS'):
    ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
SITE_ID = 1
AUTH_USER_MODEL = 'gsuser.User'

INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',

    # third party
    'corsheaders',
    'graphene_django',
    'sorl.thumbnail',
    'sortedm2m',
    'sortedm2m_filter_horizontal_widget',
    'django_json_widget',
    'rest_framework',
    'django_apscheduler',
    'solo',

    # own
    'gsuser',
    'gsmap',
    'main',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/opt/app/main/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.utils.context_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('DJANGO_DB_NAME'),
        'USER': os.getenv('DJANGO_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
        'HOST': os.getenv('DJANGO_DB_HOST', 'pdb'),
        'PORT': '5432',
        'CONN_MAX_AGE': 600,
        # 'OPTIONS': {'autocommit': True}
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

FORMAT_MODULE_PATH = 'main.formats'

STATIC_ROOT = os.environ.get('DJANGO_STATIC_DIR',
                             '/var/services/django/static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.environ.get('DJANGO_MEDIA_DIR', '/var/services/django/media')
MEDIA_URL = '/media/'
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640
FILE_UPLOAD_MAX_MEMORY_SIZE = int(15 * 1024 * 1024)  # 15 MB

GRAPHENE = {'SCHEMA': 'main.schema.schema'}

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "http://localhost:8081",
    "http://www:8000",
    "http://www.local:8000",
]
CORS_ALLOW_CREDENTIALS = True
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache',
    }
}
SESSION_COOKIE_HTTPONLY = False

THUMBNAIL_BACKEND = 'main.utils.PermalinkThumbnailBackend'
THUMBNAIL_PREFIX = 'cache/'
SCREENSHOT_SCHEDULER_CRON_MINUTES = os.environ.get('DJANGO_SCREENSHOT_SCHEDULER_CRON_MINUTES', '*')
APP_VERSION = os.environ.get('DJANGO_APP_VERSION', '')
 
