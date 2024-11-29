from .settings import *
ALLOWED_HOST = ["www.lobms.cdelmar.cl", "lobms.cdelmar.cl"]
DEBUG = True
CSRF_TRUSTED_ORIGINS = [
    'https://lobms.cdelmar.cl',
    'https://www.lobms.cdelmar.cl',  # Incluye www si lo usas
]

