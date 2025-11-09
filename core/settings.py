import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# Core Django settings
# ---------------------------

# Secret Key
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret')

# Debug
DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() == 'true'

# Allowed Hosts
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')
ALLOWED_HOSTS += ['127.0.0.1', 'localhost']
ALLOWED_HOSTS = [host for host in ALLOWED_HOSTS if host]
# Always include localhost in development or for internal Render checks
if DEBUG:
    ALLOWED_HOSTS += ['127.0.0.1', 'localhost']
if 'localhost' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append('localhost')

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ip_tracking',
    'django_ratelimit',
    'drf_yasg',  # Swagger documentation
    'django_celery_results',
    'rest_framework',  # Required for drf-yasg
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ip_tracking.middleware.IPTrackingMiddleware',
]

# URLs and WSGI
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use Postgres on production if needed
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------------------
# Celery settings
# ---------------------------
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'django-db')

# ---------------------------
# Cache settings for rate-limiting
# ---------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
RATELIMIT_USE_CACHE = 'default'
SILENCED_SYSTEM_CHECKS = ['django_ratelimit.W001', 'django_ratelimit.E003']
