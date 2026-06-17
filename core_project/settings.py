
import os
from pathlib import Path

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Set default values for the environment variables if they’re not already set
os.environ.setdefault("PGDATABASE", "memorial")
os.environ.setdefault("PGUSER", "postgres")
os.environ.setdefault("PGPASSWORD", "23Vad3r0r3029!")
os.environ.setdefault("PGHOST", "localhost")
os.environ.setdefault("PGPORT", "5432")


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["PGDATABASE"],
        'USER': os.environ["PGUSER"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ALLOWED_HOSTS = ["*"]