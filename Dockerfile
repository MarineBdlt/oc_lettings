FROM python:3.8
WORKDIR /lettingApp
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ADD . /lettingApp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /lettingApp
EXPOSE 8000
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
=======
>>>>>>> 0c930b3 (replace wgsi settings)
CMD gunicorn oc_lettings_site.settings.wsgi:application --bind 0.0.0.0:$PORT
=======
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD gunicorn oc_lettings_site.settings.wsgi:application --bind 0.0.0.0:$PORT
>>>>>>> e0f9ef8 (kj)
=======
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD gunicorn oc_lettings_site.settings.wsgi:application --bind 0.0.0.0:$PORT
>>>>>>> 0e9c3b1 (kj)
=======
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
>>>>>>> 70a555a (heroku token added in settings)
