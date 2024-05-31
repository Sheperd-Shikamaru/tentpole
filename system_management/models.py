from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    """
    UserManager - Manages user-related operations.
    """

    def create_user(self, email, password, **extra_fields):
        """

        Create and save a User with the given email and password.

        """

        if not email:

            raise ValueError(_('The Email must be set'))

        email = self.normalize_email(email)

        extra_fields.setdefault('is_staff', False)

        extra_fields.setdefault('is_superuser', False)

        extra_fields.setdefault('is_active', True)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """

        Create and save a SuperUser with the given email and password.

        """
        
        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)

        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:

            raise ValueError(_('Superuser must have is_staff=True.'))

        if extra_fields.get('is_superuser') is not True:

            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    User - Represent a user in the system
    """
    username = None

    email = models.EmailField(_('email address'), unique=True)
    
    is_superuser = models.BooleanField(default=False)
    
    is_staff = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    
    has_logged_in = models.BooleanField(default=False)
    
    

    # has_logged_in = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='system_management_user_set',  # Update the related_name
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=_('groups'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='system_management_user_set',  # Update the related_name
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __unicode__(self):

        return self.first_name + ' ' + self.last_name

    def __str__(self):

        return self.email

    def get_full_name(self):

        return self.first_name + ' ' + self.last_name
    
class Profile(models.Model):
    """
    Model representing customer information.
    """
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)