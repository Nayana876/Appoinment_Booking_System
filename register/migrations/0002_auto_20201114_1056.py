# Generated by Django 3.0.4 on 2020-11-14 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='age',
            field=models.CharField(default=12, max_length=3),
            preserve_default=False,
        ),
    ]
