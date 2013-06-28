@echo off

CALL :search
python D:\TracLight\CollabNetSVN\httpd\htdocs\update_observer\csv_to_json.py
pause


:search
del D:\TracLight\CollabNetSVN\httpd\htdocs\update_observer\update.csv
CALL :log >> update.csv
exit /b

:log
pushd \10.10.10.11
for /D /r %1 %%a in (.\*) do call :UPDATE_TIME %%a
popd
exit /b

:UPDATE_TIME
for %%i in (%1) do echo %%~pni,%%~ti
exit /b

