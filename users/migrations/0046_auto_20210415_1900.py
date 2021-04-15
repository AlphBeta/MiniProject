# Generated by Django 2.2 on 2021-04-15 13:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0045_auto_20210325_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=30)),
                ('specialization', models.CharField(blank=True, default=None, max_length=25)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=15, region=None)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('email', models.EmailField(max_length=254)),
                ('document', models.URLField()),
                ('postal_code', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='postal_code',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='medinfo',
            name='eye_sight',
            field=models.CharField(choices=[('Normal', 'I can see clearly'), ('Hypermetropia', 'Difficult in reading'), ('Presbyopia', 'Difficulty in both'), ('Glasses', 'I wear Glasses'), ('Myopia', 'Difficult to see distant objects')], default=False, max_length=20, verbose_name='How is your eye sight?'),
        ),
        migrations.AlterField(
            model_name='medinfo',
            name='pulse',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Resting Heart Rate'),
        ),
    ]