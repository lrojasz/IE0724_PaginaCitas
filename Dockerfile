# Construya esta imágen con:
# docker build --tag ie-0724/paginacitas:0.1.4 .

# Corra esta imágen con:
# docker run -p 8000:8000 -ti ie-0724/paginacitas:0.1.4

# Definimos OS base
FROM ubuntu:20.04

# Variables de tiempo y ubicación para la imágen
ENV TZ=America/Costa_Rica
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Algo de información
LABEL mantainer="laura.rojaszumbado@ucr.ac.cr"
LABEL version="1.0"
LABEL description="Custom docker image for a Django project"

# Elegir usuario root e instalar
USER root
RUN apt-get update \
    && apt-get --yes --no-install-recommends install apt-utils\
    && apt-get --yes --no-install-recommends install vim \
    && apt-get --yes --no-install-recommends install python3 \
    && apt-get --yes --no-install-recommends install python3-pip \
    && pip3 install django \
    && apt-get --yes --no-install-recommends install python3-django

# Actualizar django usando pip: RUN pip install --upgrade django

# Crear carpeta del proyecto
RUN mkdir -p /usr/src

# Copiar archivos de forma ordenada
COPY GimnasioIE0724 /usr/src/GimnasioIE0724
#COPY include /usr/src/GimnasioIE0724/appointments
#COPY include /usr/src/GimnasioIE0724/static
#COPY manage.py /usr/src/CascoConvexo/manage.py
#COPY db.sqlite3 /usr/src/CascoConvexo/db.sqlite3

# Ir a la carpeta de gimnasio
RUN cd /usr/src/GimnasioIE0724 \
    && python3 manage.py makemigrations

# Ir a la carpeta de gimnasio
RUN cd /usr/src/GimnasioIE0724 \
    && python3 manage.py migrate

# Declarar WORKDIR
WORKDIR /usr/src/GimnasioIE0724
EXPOSE 8000
RUN chown -R $USER:$USER .

#python3 manage.py runserver 127.0.0.1:8000