from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.fields import AutoField
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, username, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not username:
            raise ValueError('The username must be set')

        user = self.model(email=email,
                          username=username, ** extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email, username, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)


# class CustomUser(AbstractUser):
#     username = models.CharField(
#         _('username'), primary_key=True,  max_length=50, unique=True)
#     email = models.EmailField(_('email address'), unique=True)
#     image = models.ImageField(
#         upload_to='accounts/profile_pics', blank=True, default='default.jpg')

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     objects = CustomUserManager()

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.username


class CustomUser(AbstractUser):

    image = models.ImageField(
        upload_to='accounts/profile_pics', blank=True, default='default.jpg')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        print(instance)
        Token.objects.create(user=instance)
