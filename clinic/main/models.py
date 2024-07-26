from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class Person(models.Model):
    name = models.CharField('Имя', max_length=50)
    phone = models.TextField('Номер телефона', max_length=50)

    class Meta:
        abstract = True

class Doctor(Person):
    username = models.CharField('Логин', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Докторы'


class Appointment(models.Model):
    name = models.CharField('Имя', max_length=100, default='')
    phone = models.CharField('Номер телефона', max_length=17,
                             blank=True, default='')
    status = models.CharField('Статус заявки', max_length=50,
                              default='В обработке')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Service(models.Model):
    name = models.CharField('Наименование услуги', max_length=50)
    price = models.FloatField('Цена услуги')
    description = models.TextField('Описание', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class CustomUser(AbstractUser):
    phone = models.CharField('Номер телефона', max_length=17, blank=True,
                             default='')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Уникальное имя для обратной связи
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Уникальное имя для обратной связи
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
