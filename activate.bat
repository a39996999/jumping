@echo off
FOR /F "delims=: tokens=2" %%a in ('ipconfig ^| find "IPv4"') do set _IPAddress=%%a
start cmd /k "conda.bat activate django_py37 & cd/d C:\jumping_site & python manage.py runserver %_IPAddress%:8080"
start cmd /k "conda.bat activate django_py37 & cd/d C:\jumping_site & celery -A jumping_site purge -f & celery -A  jumping_site worker -l info"

