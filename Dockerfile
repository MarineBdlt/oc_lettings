FROM python:3.8
WORKDIR /lettingApp
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ADD . /lettingApp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /lettingApp
EXPOSE 8000
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT