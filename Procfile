release: python manage.py migrate
web: daphne FTC_project.asgi:application --port $PORT --bind 0.0.0.0 -v2 
worker: python manage.py runworker channels --settings=django_project.settings -v2

