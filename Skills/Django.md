# Commands
## Run the server
python manage.py runserver 0:8000
(allow host in myproject/settings.py)
## Create new app
python manage.py startapp polls
## Migrations - Required if models change
python manage.py makemigrations polls
python manage.py migrate

## Apache WSGI
1. define relative WSGIPythonPath to django project -> see django-apache2-docker/demo_site.conf
2. Add wsgi.py file in demo_site/demo_site/ & link to demo_site.settings
3. Add WSGI_APPLICATION = 'demo_site.wsgi.application' in demo_site/demo_site/settings.py
4. Rebuild Dockerfile
5. Enjoy?


