# Generated by Django 4.2 on 2023-04-18 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='data',
            new_name='date',
        ),
    ]
