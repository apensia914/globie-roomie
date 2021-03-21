from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ''' Custom User Model '''

    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.Field.choices
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
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True, default=GENDER_MALE) #3.2 null: Database, blank: Admin
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True, default=LANGUAGE_KOREAN)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, null=True, default=CURRENCY_USD)
    superhost = models.BooleanField(default=False)