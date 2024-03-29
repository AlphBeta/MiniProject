# Generated by Django 2.2 on 2021-02-10 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_profile_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=2, max_digits=3, null=True, verbose_name='Height(in cm)')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=3, null=True, verbose_name='Height(in cm)')),
                ('donate', models.BooleanField(default=False, verbose_name='Willing to donate?')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
    ]
