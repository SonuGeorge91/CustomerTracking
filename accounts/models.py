from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class AbstractBase(models.Model):
    id = models.UUIDField(primary_key=True,
    default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class CustomUserManager(BaseUserManager):
    """ Custom user manager where email is the unique identifiers
        for authentication instead of username """

    def create_user(self, email, password, **extra_fields):
        """ Create and save User with given email and password """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fileds):
        """Create and save super user with the given email and password"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('username', email)

        if extra_fileds.get('is_staff') is not True:
            raise ValueError(_('Super User must have is_staff=True.'))
        if extra_fileds.get('is_superuser') is not True:
            raise ValueError(_('Super User must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fileds)

class Users(AbstractUser, AbstractBase):
    email = models.EmailField(_('email'), unique=True)
    password = models.CharField(_('password'), max_length=128, 
    null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = "ctracker_users"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.email