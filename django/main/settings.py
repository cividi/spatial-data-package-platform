import os
import os.path
import graphene

from django.utils.translation import gettext_lazy as _

# use your own secret_key, default for testing and dev
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY') or os.getenv('DJANGO_SECRET_KEY_DEV')
HOST = os.getenv('DJANGO_HOST', 'www.local:8000')
INTERNAL_HOST = os.getenv('DJANGO_INTERNAL_HOST', 'http://django:8081')
DEBUG = os.getenv('DJANGO_DEBUG') == 'true'
USE_HTTPS = os.getenv('DJANGO_HTTPS') == 'true'
DB_SEARCH_PATH = os.getenv('DJANGO_DB_SEARCH_PATH', 'public')
OIDC_ACTIVE = os.getenv('DJANGO_OIDC_LOGIN', False) == 'true'


if USE_HTTPS:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # SECURE_SSL_REDIRECT = True

DEFAULT_FROM_EMAIL = os.environ.get('DJANGO_DEFAULT_FROM_EMAIL', 'noreply@www.local')
EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST', 'maildev')
EMAIL_PORT = int(os.environ.get('DJANGO_EMAIL_PORT', 25))
EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_HOST_PASSWORD', '')
EMAIL_USE_SSL = True if EMAIL_PORT == 465 else False
ADMINS = os.environ.get('DJANGO_ADMINS', 'admin@local.lan').split(',')
ADMINS = list(zip(ADMINS, ADMINS))
MANAGERS = ADMINS
ADMIN_NAME = os.environ.get('DJANGO_ADMIN_NAME', 'gemeindescan DEV')
ADMIN_HEADER_COLOR = os.environ.get('DJANGO_ADMIN_HEADER_COLOR', '#543076')
LOGIN_PAGE_TITLE = os.environ.get('LOGIN_PAGE_TITLE', 'Gemeindescan')

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
    'django_jsonform',
    'rest_framework',
    'django_apscheduler',
    'solo',
    'parler',
    'markdownx',

    # own
    'gsuser',
    'gsmap',
    'main',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


if OIDC_ACTIVE:
    OIDC_OP_LOGOUT_URL_METHOD = 'main.utils.oidc_op_logout'
    OIDC_USERNAME_ALGO = 'main.utils.generate_username'
    OIDC_RP_SIGN_ALGO = 'RS256'
    OIDC_RP_SCOPES = 'openid email'

    LOGIN_URL = 'oidc_authentication_init'
    LOGIN_REDIRECT_URL = '/gmanage'
    LOGOUT_REDIRECT_URL = '/gmanage'

    INSTALLED_APPS += [ 'mozilla_django_oidc', ]
    MIDDLEWARE += [ 'mozilla_django_oidc.middleware.SessionRefresh', ]
    AUTHENTICATION_BACKENDS = [
        'gsuser.auth.OIDCAuthenticationBackend',
        'django.contrib.auth.backends.ModelBackend',
    ]

    OIDC_RP_CLIENT_ID = os.getenv('OIDC_RP_CLIENT_ID', None)
    OIDC_RP_CLIENT_SECRET = os.getenv('OIDC_RP_CLIENT_SECRET', None)

    OIDC_OP_AUTHORIZATION_ENDPOINT = os.getenv('OIDC_OP_AUTHORIZATION_ENDPOINT',
        'https://auth.dfour.io/auth/realms/dfour/protocol/openid-connect/auth')
    OIDC_OP_TOKEN_ENDPOINT = os.getenv('OIDC_OP_TOKEN_ENDPOINT',
        'https://auth.dfour.io/auth/realms/dfour/protocol/openid-connect/token')
    OIDC_OP_USER_ENDPOINT = os.getenv('OIDC_OP_USER_ENDPOINT',
        'https://auth.dfour.io/auth/realms/dfour/protocol/openid-connect/userinfo')
    OIDC_OP_JWKS_ENDPOINT = os.getenv('OIDC_OP_JWKS_ENDPOINT',
        'https://auth.dfour.io/auth/realms/dfour/protocol/openid-connect/certs')
    OIDC_OP_LOGOUT_ENDPOINT = os.getenv('OIDC_OP_LOGOUT_ENDPOINT',
        'https://auth.dfour.io/auth/realms/dfour/protocol/openid-connect/logout')

REST_FRAMEWORK = {
    # Only enable JSON renderer by default.
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

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
        'OPTIONS': {
            'options': f"-c search_path={DB_SEARCH_PATH}",
        }
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

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = ( 'locale', )

LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
    ('fr', 'French'),
    ('it', 'Italian'),
]

PARLER_LANGUAGES = {
    1: (
        {'code': 'de',},
        {'code': 'en',},
        {'code': 'fr',},
        {'code': 'it',},
    ),
    'default': {
        'fallback': 'de',             # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,   # the default; let .active_translations() return fallbacks too.
    }
}

PARLER_DEFAULT_LANGUAGE_CODE = 'de'

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
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8081",
    "http://www:8000",
    "http://www.local:8000",
]
if os.environ.get('DJANGO_ALLOWED_HOSTS'):
    CORS_ALLOWED_ORIGINS += [
        f"http://{h}" for h in ALLOWED_HOSTS if not h.startswith('.')
    ]
    CORS_ALLOWED_ORIGINS += [
        f"https://{h}" for h in ALLOWED_HOSTS if not h.startswith('.')
    ]
    CORS_ALLOWED_ORIGIN_REGEXES = [
        f"^http://[a-z0-9-]+{h}$".replace(".","\.") for h in ALLOWED_HOSTS if h.startswith('.')
    ]
    CORS_ALLOWED_ORIGIN_REGEXES += [
        f"^https://[a-z0-9-]+{h}$".replace(".","\.") for h in ALLOWED_HOSTS if h.startswith('.')
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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'mozilla_django_oidc': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
    }
}

# Celery Configuration Options
CELERY_TIMEZONE = "Europe/Zurich"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 10 * 60

CELERY_RESULT_SERIALIZER = 'json'

CELERY_BROKER_URL = os.getenv('CELERY_BROKER', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = os.getenv('CELERY_BACKEND', 'redis://redis:6379/0')

API_CACHE_ROOT = '/var/services/django/cache'

Q_LANGUAGE = graphene.Enum(
    "LanguageCodeEnum",
    [(lang[0], lang[1]) for lang in LANGUAGES],
)
