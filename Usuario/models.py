from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def _create_user(self, username, email, nombres, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            nombres=nombres,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, nombres, password=None, **extra_fields):
        return self._create_user(username, email, nombres, password, False, False, **extra_fields)

    def create_superuser(self, username, email, nombres, password=None, **extra_fields):
        return self._create_user(username, email, nombres, password, True, True, **extra_fields)





class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique=True, max_length=150)
    email = models.EmailField('Correo electrónico', max_length=254, unique=True)
    nombres = models.CharField(' Nombres', max_length=200, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return self.nombres + " " + self.apellidos




