# Partir de l'image Python 3.9-slim-bullseye
FROM python:3.9-slim-bullseye

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Copier les fichiers de requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances requises en utilisant pip
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier le code source de votre application dans le conteneur
COPY . .

# Définir le port sur lequel votre application Django écoutera
EXPOSE 8000

# Démarrer l'application en exécutant la commande suivante
# Démarrer en mode serveur Django normal
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Démarer en mode gunicorn (serveur local sur 127.0.0.1:8000)
CMD gunicorn oc_lettings_site.wsgi:application --log-file=- --bind 0.0.0.0:8000