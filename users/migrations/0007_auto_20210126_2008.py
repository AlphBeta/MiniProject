# Generated by Django 2.2 on 2021-01-26 14:38

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210124_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='phone_no',
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=None, max_length=8),
        ),
        migrations.AddField(
            model_name='profile',
            name='emergency_contact',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=15, region=None),
        ),
    ]
