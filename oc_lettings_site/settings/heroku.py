"""
Production Settings for Heroku
"""

from oc_lettings_site.settings.base import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://b78c3fb5520f4aa387d7cd89da439647@o1401908.ingest.sentry.io/6733392",
    integrations=[
        DjangoIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)

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

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# SENTRY, CREER PROJET DJANGO, RECUPERER CODE A COLLER DANS LES SETTINGS
# ADRESSE NOMINATIVE A METTRE DANS L'ENVIRONNEMENT DE HEROKU
