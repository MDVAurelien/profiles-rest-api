from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # Log user with email and not name
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_ful_name(self):
        """Retrieve the full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve the short name of user"""
        return self.name

    def __str__(self):
        """Return String representation of our user"""
        return self.email

