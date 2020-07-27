from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.
class MinervaUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_('El email es necesario'))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user



class MinervaUser(AbstractBaseUser, PermissionsMixin):
    """
    Usuario Custom para Minerva LMS
    """
    email = models.EmailField(max_length=254, blank=False, unique=True)
    first_name = models.CharField(max_length=254, blank=False)
    last_name = models.CharField(max_length=254, blank=False )
    photo = models.ImageField(upload_to='users/profile/photos', blank=True)
    avatar = models.ImageField(upload_to='users/profile/avatars', blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    institutional_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MinervaUserManager()


    def get_full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

    def get_email(self):
        return self.email