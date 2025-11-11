from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager


class CustomUser(AbstractUser, PermissionsMixin):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("-date_joined",)

    username = None
    email = models.EmailField(verbose_name="Электронная почта", unique=True, blank=False, null=False)
    phone_number = PhoneNumberField(verbose_name="Номер телефона",)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{str(self.email) or self.first_name}'