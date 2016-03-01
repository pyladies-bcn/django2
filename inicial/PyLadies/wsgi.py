"""
WSGI config for PyLadies project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/home/elena/djangostack-1.8.9-0/apps/django/django_projects/PyLadies')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/elena/djangostack-1.8.9-0/apps/django/django_projects/PyLadies/egg_cache")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PyLadies.settings")

application = get_wsgi_application()
