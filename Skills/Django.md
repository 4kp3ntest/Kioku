# Run the server
python manage.py runserver 0:8000
(allow host in myproject/settings.py)

# Create new app
python manage.py startapp polls

# Required if models change
python manage.py makemigrations polls
python manage.py migrate
