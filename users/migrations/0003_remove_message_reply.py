# Generated by Django 3.2.12 on 2022-03-14 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_message_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='reply',
        ),
    ]
