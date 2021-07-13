from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
# Create your models here.


# class User(AbstractUser, auth.models.PermissionsMixin):

#     image = models.ImageField(upload_to='accounts/images')

#     def __str__(self):
#         return '@{}'.format(self.username)

# class User(auth.models.User, auth.models.PermissionsMixin):

#     def __str__(self):
#         return '@{}'.format(self.username)

# https://github.com/akjasim/cb_dj_custom_user_model/blob/master/README.md
# https://www.youtube.com/watch?v=SbU2wdPIcaY&list=LL&index=1&t=218s&ab_channel=CodeBand

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, username, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not username:
            raise ValueError('The username must be set')
        # username = self.username
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


class CustomUser(AbstractUser):
    username = models.CharField(
        _('username'), primary_key=True,  max_length=50, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(
        upload_to='accounts/profile_pics', blank=True, default='default.jpg')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
