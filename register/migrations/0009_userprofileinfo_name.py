# Generated by Django 3.0.4 on 2020-11-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20201118_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='Name',
            field=models.CharField(default=1, max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
