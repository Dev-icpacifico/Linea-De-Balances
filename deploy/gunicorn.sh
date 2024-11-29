#!/bin/bash
NAME="lobms"
DJANGODIR=/home/developer/Linea-De-Balances  # Ruta absoluta del directorio del proyecto
SOCKFILE=/tmp/gunicorn-lobms.sock
LOGDIR=${DJANGODIR}/logs/gunicorn.log
USER=developer
GROUP=developer
NUM_WORKERS=5

# Asegúrate de que esta ruta coincida con la ubicación del archivo wsgi.py
DJANGO_WSGI_MODULE=LineaBalance.wsgi

# Eliminar socket anterior
rm -frv $SOCKFILE

# Crear directorio de logs si no existe
mkdir -p $(dirname $LOGDIR)

# Depuración
echo "Starting Gunicorn..."
echo "Project Directory: $DJANGODIR"
echo "WSGI Module: $DJANGO_WSGI_MODULE"
echo "Socket File: $SOCKFILE"

# Cambiar al directorio del proyecto
cd $DJANGODIR

# Ejecutar Gunicorn
exec ${DJANGODIR}/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR
