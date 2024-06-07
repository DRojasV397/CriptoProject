Las dependencias del proyecto se instalan con:
    pip install -r requirements.txt

Si se añaden depencias hay que actualizar el archivo requirements.txt con:
    pip freeze > requirements.txt

Antes de correr el progarama se debe acceder a la consola de MySQL y ejecutar los siguiente comandos:
    CREATE DATABASE flask_app;
    CREATE USER 'flask_user'@'localhost' IDENTIFIED BY 'your_password';
    GRANT ALL PRIVILEGES ON flask_app.* TO 'flask_user'@'localhost';
    FLUSH PRIVILEGES;