# Generated by Django 2.2.9 on 2020-01-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_maintenance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='date',
            field=models.DateField(verbose_name='Vehicle last checked on'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintain',
            field=models.CharField(choices=[('R', 'Running'), ('A', 'Available for Sale')], default='R', max_length=10, verbose_name='Maintenance Type'),
        ),
    ]
