from .base import *

env_name = os.getenv("ENV_NAME", "local")

print("ENV_NAME", env_name)

if env_name == "heroku":
    from .heroku import *
else:
    from .local import *
