# Generated by Django 3.0.4 on 2020-11-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20201118_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='Name',
            field=models.CharField(max_length=300, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Address'),
        ),
    ]
