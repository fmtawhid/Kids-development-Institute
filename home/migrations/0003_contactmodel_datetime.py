# Generated by Django 5.0.6 on 2024-05-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='dateTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
