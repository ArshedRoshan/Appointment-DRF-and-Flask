# Generated by Django 4.2 on 2023-04-19 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Account_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Describe_company',
        ),
        migrations.RemoveField(
            model_name='user',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follow',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='user',
            name='hiring_for',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_block',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_follow',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_follower',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_verfied',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]