# Generated by Django 3.2.9 on 2021-12-10 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_emailconfirmation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_confirmed',
        ),
        migrations.DeleteModel(
            name='EmailConfirmation',
        ),
    ]
