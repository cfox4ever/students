from django.db import models
from simple_history.models import HistoricalRecords
from .setups import STATES,status,locationStatus
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.contrib.auth.models import PermissionsMixin

from django.utils import timezone
from crum import get_current_user
from .managers import CustomUserManager


class Branch(models.Model):
    
    
    name        = models.CharField(max_length=250 , null=True)
    phone       = models.CharField(max_length=12,blank=True,
                                    help_text='Contact phone number', null=True)
    address_1   = models.CharField(max_length=128, null=True)
    address_2   = models.CharField(max_length=128, blank=True, null=True)

    city        = models.CharField(max_length=64, null=True)
    state       = models.CharField(max_length=200,choices=STATES , null=True)
    zip_code    = models.CharField(max_length=50, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    status      = models.BooleanField()
    history     = HistoricalRecords()
    def __str__(self):
        return self.name

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email          = models.EmailField('email address', unique=True)
    username       = models.CharField(max_length=20, blank=True,unique=True)
    is_staff       = models.BooleanField(default=False)
    emailConfirmed = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=False)
    date_joined    = models.DateTimeField(default=timezone.now)
    first_name     = models.CharField(max_length=20, blank=True)
    last_name      = models.CharField(max_length=20, blank=True)
    contact_no     = models.CharField(max_length=20, blank=True)
    role           = models.CharField(max_length=300, blank=True)
    branch         = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    history        = HistoricalRecords()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    
    def __str__(self):
        return (self.username)

    
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
  

    
    
