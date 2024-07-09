from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


import uuid
USER_CHOICES = (
    ('Admin','Admin'),
    ('SalesManager', 'SalesManager'),
    ('SalesPerson', 'SalesPerson'),
)

REFERENCE_CHOICES = (
    ('Reference','Reference'),
    ('Google','Google'),
    ('Facebook','Facebook'),
    ('Youtube','Youtube'),
    ('Trade Fair','Trade Fair'),
    ('LinkedIn','LinkedIn'),
    ('Email','Email'),
    ('PhoneCall','PhoneCall'),
    ('SMS','SMS'),
    ('TeamTravolltCrm','Team Travollt Crm'),
)


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    contact_no = PhoneNumberField(_('contact number'), max_length=20)
    country = CountryField(blank_label='(select country)')
    area = models.CharField(max_length=30,null=True,blank=True)
    referral = models.CharField(max_length=30,choices=REFERENCE_CHOICES,default='Reference')
    type = models.CharField(max_length=20, choices=USER_CHOICES, default='Admin')
    website = models.URLField(max_length=200,blank=True)
    is_internaluser = models.BooleanField(default=False)
    
 