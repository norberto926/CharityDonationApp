# Generated by Django 4.1.7 on 2023-03-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_alter_user_managers_alter_donation_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
