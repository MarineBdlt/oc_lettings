"""
Production Settings for Heroku
"""
# flake8: noqa: F403 , F405 # Bypass Flake8 star import
# If using in your own project, update the project namespace below

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

from oc_lettings_site.settings.base import *

# Configure Sentry SDK
# sentry_sdk.init(
#     dsn=env("SENTRY_DSN"),
#     integrations=[DjangoIntegration()],
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=1.0,
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True,
#     release="oc-lettings-manu512@1." + env("BUILD_NUMBER"),
# )

# False if not in os.environ
DEBUG = env("DEBUG")

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# RENTRER DANS ENV VARIABLES HEROKU
