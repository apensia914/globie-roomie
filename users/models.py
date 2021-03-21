import uuid #16.2 
from django.core.mail import send_mail #16.2
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings #16.2 

class User(AbstractUser):

    ''' Custom User Model '''

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
    )

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_KOREAN = 'kr'
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_KOREAN, 'Korean'),
    )

    CURRENCY_USD = 'usd'
    CURRENCY_KRW = 'krw'
    CURRENCY_CHOICES = (
        (CURRENCY_USD, 'usd'),
        (CURRENCY_KRW, 'krw'),
    )

    bio = models.TextField(default="", blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True, default=GENDER_MALE) 
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True, default=LANGUAGE_KOREAN)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, null=True, default=CURRENCY_USD)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True) 

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret 
            send_mail('Verify Globie-Roomie Account', f'Verify account, this is your secret: {secret}', settings.EMAIL_FROM, [self.email], fail_silently=False)
        return 