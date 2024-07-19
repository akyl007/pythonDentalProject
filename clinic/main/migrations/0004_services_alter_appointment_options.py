# Generated by Django 5.0.7 on 2024-07-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_appointment_patient_remove_appointment_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование услуги')),
                ('price', models.FloatField(verbose_name='Цена услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
    ]
