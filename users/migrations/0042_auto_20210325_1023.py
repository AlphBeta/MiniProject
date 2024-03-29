# Generated by Django 2.2 on 2021-03-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_auto_20210325_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medinfo',
            name='eye_sight',
            field=models.CharField(choices=[('Glasses', 'I wear Glasses'), ('Hypermetropia', 'Difficult in reading'), ('Myopia', 'Difficult to see distant objects'), ('Presbyopia', 'Difficulty in both'), ('Normal', 'I can see clearly')], default=False, max_length=20, verbose_name='How is your eye sight?'),
        ),
        migrations.AlterField(
            model_name='medinfo',
            name='fever_cycle',
            field=models.CharField(choices=[('S', 'Very Often'), ('NN', "Don't remember the last time I got"), ('N', 'Once in a while')], default=None, max_length=3, null=True, verbose_name='How often do you get cold or fever?'),
        ),
    ]
