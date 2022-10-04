web: gunicorn main_file.wsgi
release: python manage.py migrate
release: python manage.py collectstatic
release: python manage.py createsuperuser