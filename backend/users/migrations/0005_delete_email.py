# Generated by Django 3.2.9 on 2021-12-09 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
    ]
