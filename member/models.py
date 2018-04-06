from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(u'닉네임', max_length=10, blank=False, default='')
    GENDER_CHOICES = (
        ('선택 안 함', '선택 안 함'),
        ('여성', '여성'),
        ('남성', '남성'),
    )
    gender = models.CharField('성별(선택사항)', max_length=10, choices=GENDER_CHOICES, default='N')
    zipCode = models.PositiveIntegerField('우편주소', null=True)
    address = models.CharField('주소', max_length=50, default='')
    detailedAddress = models.CharField('상세주소', max_length=50, default='', null=True, blank=True)
    phone_nember = models.CharField(blank=False,default='',max_length=13)

    def __str__(self):
        return self.username