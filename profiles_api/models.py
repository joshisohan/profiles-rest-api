from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """ Define how to manage a UserProfile operation. """

    def create_user(self, email, name, password):
        """ define a normal user """
        if not email:
            raise ValueError('Please provide an email address')

        if not name:
            raise ValueError('Please provide a name')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Create a super user with admin access. """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ This is a model user class """

    email = models.EmailField(max_length=256, unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ This return the full username """
        return self.name

    def get_short_name(self):
        """ This return the short name of user """
        return self.name

    def ___str__(self):
        """ This is the string representation of UserProfile class object """
        return self.name


