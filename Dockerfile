# Construya esta imágen con:
# docker build --tag ie-0724/paginacitas:0.0.1 .

# Corra esta imágen con:
# docker run -ti ie-0724/paginacitas:0.0.1

# Definimos OS base
FROM ubuntu:20.04

# Variables de tiempo y ubicación para la imágen
ENV TZ=America/Costa_Rica
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Algo de información
LABEL mantainer="laura.rojaszumbado@ucr.ac.cr"
LABEL version="1.0"
LABEL description="Custom docker image for a Gtest example"

# Elegir usuario root e instalar
USER root
RUN apt-get update \
    && apt-get --yes --no-install-recommends install vim \
    && apt-get --yes --no-install-recommends install python3 \
    && apt-get --yes --no-install-recommends install python3-pip \
    && pip3 --yes --no-install-recommends install django
    #&& sudo apt --yes --no-install-recommends install -python3-django

# Actualizar django usando pip: RUN pip install --upgrade django

# Crear carpeta del proyecto
RUN mkdir -p /usr/src/PaginaCitas

# Copiar archivos de forma ordenada
COPY include /usr/src/PaginaCitas/gymnasium
COPT include /usr/src/PaginaCitas/appointments
#COPY CMakeLists.txt /usr/src/CascoConvexo/CMakeLists.txt

# Ir a la carpeta de gimnasio
RUN cd /usr/src/PaginaCitas/gimnasio 

# aplicar migrate?&& python3 manage.py migrate
#python3 manage.py runserver 
#[port] va a correr en el punto 8000