@echo off
FOR /F "delims=: tokens=2" %%a in ('ipconfig ^| find "IPv4"') do set ip_=%%a
for /f "tokens=* delims= " %%i in ("%ip_%") do set "ip_=%%i"
set ip_=http://%ip_%:8080	
start cmd /c "conda.bat activate django_py37 & cd/d D:\jumping_site & python make_qrcode.py %ip_%"