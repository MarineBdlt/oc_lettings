from .base import *

env_name = os.getenv("ENV_NAME", "heroku")

print("ENV_NAME", env_name)

if env_name == "heroku":
    from .heroku import DEBUG, ALLOWED_HOSTS, SECRET_KEY
else:
    from .local import DEBUG, ALLOWED_HOSTS, SECRET_KEY

# FALKE 8 IGNORE IMPORT * !!!!!!!!!!!
# --> Check deplooy config.yml
# --> "heroku env" is nowhere
# --> nettoyer, clarifier, commenter
# ---> deploy on heroku CHECK DOC
