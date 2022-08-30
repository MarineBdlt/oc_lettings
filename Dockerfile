# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /LettingsApp
COPY requirements.txt .
COPY . /LettingsApp
RUN pip install -r requirements.txt
EXPOSE 8000
# CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
CMD python manage.py runserver

# ANCHOR 
# OK BUILD EN LOCAL
# OK RUN DOCKER EN LOCAL
# --- CREER PROJET SUR CIRCLE CI ATTACHE AU REPERTOIRE GITHUB : machine virtuelle pour lancer des actions
# CI (pour tester intégration) CL (pour tester déployement)
# fichier.yml : script pour lancer des tests
# LANCER LES TESTS, BUILD ET PUSH DOCKER VERS DOCKER HUB, DEPLOYER SUR HEROKU