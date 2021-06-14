# IE0724_PaginaCitas
Un repositorio de GitHub que contiene todo el código necesario para desarollar la página web de citas den proyecto 2, usando la herramienta Django.

## Docker
Para inicializar y correr la imágen de Docker, se debe utilizar lo siguiente:

``docker build --tag ie-0724/paginacitas:0.1.4 .``

``docker run -p 8000:8000 -ti ie-0724/paginacitas:0.1.4``

## Django
Para correr el servidor, solo se tiene permitido como host la dirección 0.0.0.0:8000. Por lo tanto, se utiliza la siguiente instrucción: 

``python3 manage.py runserver 0.0.0.0:8000 ``
