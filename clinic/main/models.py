from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Group


class Doctor(models.Model):
        name = models.CharField('Имя', max_length=50)
        login = models.CharField('Логин', max_length=50)
        phone = models.TextField('Номер телефона', max_length=50)

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Доктор'
            verbose_name_plural = 'Докторы'

class Appointment(models.Model):
    name = models.CharField('Имя',max_length=100,default='')
    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Номер телефона должен быть в формате: '+999999999'. Допускается до 15 цифр.")
    phone = models.CharField('Номер телефона',validators=[phone_validator], max_length=17, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural  = 'Заявки'

class Service(models.Model):
    name = models.CharField('Наименование услуги', max_length=50)
    price = models.FloatField('Цена услуги')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'



class CustomUser(AbstractUser):
    phone = models.CharField('Номер телефона', max_length=17, blank=True, default='')

    def __str__(self):
        return self.username