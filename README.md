# Proyecto-Streaming

## -- Guia de instalacion --

### Crear el usuario mysql de la siguiente forma:

- Abrir el terminal y escribir:
-   ```
    sudo service mysql start
    ```
- Ingresar con su usuario (mysql -u suUsuario -p) y luego escribir
-   ```
    CREATE USER 'grupo10'@'localhost' IDENTIFIED BY 'pepe1234';
    ```
-   ```
    GRANT ALL PRIVILEGES ON * . * TO 'grupo10'@'localhost';
    ```
-   ```
    FLUSH PRIVILEGES;
    ```
