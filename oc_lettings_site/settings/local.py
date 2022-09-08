# flake8: noqa: F403 , F405 # Bypass Flake8 star import
from oc_lettings_site.settings.base import *

# from oc_lettings_site.settings import env

# False if not in os.environ
DEBUG = True
# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
# Take environment variables from .env file
SECRET_KEY = env("SECRET_KEY")
# PASSWORD = env("PASSWORD")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
