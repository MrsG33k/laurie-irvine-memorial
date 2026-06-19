"""
WSGI config for core_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth.models import User


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')

# Check if the user already exists first so the app doesn't crash on reload
if not User.objects.filter(username='jennie').exists():
    User.objects.create_superuser(
        username='admin',
        email='jenki2@gmail.com',
        password='Monday10!'
    )

application = get_wsgi_application()

