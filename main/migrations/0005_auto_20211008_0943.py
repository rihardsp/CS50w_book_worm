# Generated by Django 2.0.2 on 2021-10-08 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211008_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emails',
            old_name='email',
            new_name='user_email',
        ),
        migrations.RenameField(
            model_name='emails',
            old_name='name',
            new_name='user_name',
        ),
    ]
