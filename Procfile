release: python manage.py migrate
web: hypercorn FTC_project.asgi:application 
worker: python manage.py runworker channels --settings=django_project.settings -v2

