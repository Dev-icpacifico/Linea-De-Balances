from pathlib import Path

# BASE_DIR debería estar definido como Path
BASE_DIR = Path(__file__).resolve().parent.parent



DATABASES_POSTGRESQL = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'lineabalance',
    'USER': 'postgres',
    'PASSWORD': 'postgresql',
    'HOST': '127.0.0.1',
    'PORT': '5432',
}
DATABASES_POSTGRESQL_PRODUCCION = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'lobms_produccion',
    'USER': 'postgres',
    'PASSWORD': 'YouShallNotPass409#',
    'HOST': '127.0.0.1',
    'PORT': '5432',
}
DATABASES_POSTGRESQL_TEST_V2 = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'lobms_desarrollo',
    'USER': 'postgres',
    'PASSWORD': 'postgresql',
    'HOST': '127.0.0.1',
    'PORT': '5432',
}
# Configuración de SQLite
DATABASES_SQLITE = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}
