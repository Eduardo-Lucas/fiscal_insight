from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome


class UserManager(BaseUserManager):
    def create_user(self, email, empresa, password=None, **extra_fields):
        if not email:
            raise ValueError("Email é obrigatório.")
        if not empresa:
            raise ValueError("Usuário deve estar associado a uma empresa.")
        email = self.normalize_email(email)
        user = self.model(email=email, empresa=empresa, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        empresa = Empresa.objects.first()
        user = self.create_user(email, empresa, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="usuarios")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['empresa']

    objects = UserManager()

    def __str__(self):
        return self.email
