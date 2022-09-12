import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD:oc_lettings_site/asgi.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings.heroku")
>>>>>>> a9739f9 (kjk):oc_lettings_site/settings/asgi.py

application = get_asgi_application()
