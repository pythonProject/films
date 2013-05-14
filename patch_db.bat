"C:\Program Files\MySQL\MySQL Server 5.5\bin\mysql.exe" -uroot -p < create_database.sql
"C:\Program Files\MySQL\MySQL Server 5.5\bin\mysql.exe" -ufilms -pfilms films < films.sql
rd /S /Q "D:\work\pythonDevelopment\films\films_project\films_app\static\media\images"
rd /S /Q "D:\work\pythonDevelopment\films\films_project\films_app\static\media\movies"
md "D:\work\pythonDevelopment\films\films_project\films_app\static\media\images"
md "D:\work\pythonDevelopment\films\films_project\films_app\static\media\movies"