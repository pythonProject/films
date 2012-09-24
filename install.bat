@ echo off

echo creating D:\work\pythonDevelopment folder
md D:\work
md D:\work\pythonDevelopment
D:
cd work\pythonDevelopment

pause>null
echo clonning the films repository
git clone git@github.com:pythonProject/films.git

pause>null
echo creating database
rem mysql -uroot -p < create_database.sql

pause>null
echo synchronizing database with django requirements
python manage.py syncdb

pause>null
python manage.py runserver