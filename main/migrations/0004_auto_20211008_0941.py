# Generated by Django 2.0.2 on 2021-10-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_emails_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='emails',
            name='email',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='emails',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
