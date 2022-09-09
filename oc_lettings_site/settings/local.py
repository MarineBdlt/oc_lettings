from oc_lettings_site.settings.base import *

# False if not in os.environ
DEBUG = True

# Take environment variables from .env file
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
