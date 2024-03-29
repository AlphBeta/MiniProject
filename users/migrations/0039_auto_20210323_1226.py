# Generated by Django 2.2 on 2021-03-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_auto_20210323_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='medinfo',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=None, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='medinfo',
            name='eye_sight',
            field=models.CharField(choices=[('Normal', 'I can see clearly'), ('Glasses', 'I wear Glasses'), ('Hypermetropia', 'Difficult in reading'), ('Presbyopia', 'Difficulty in both'), ('Myopia', 'Difficult to see distant objects')], default=False, max_length=20, verbose_name='How is your eye sight?'),
        ),
        migrations.AlterField(
            model_name='medinfo',
            name='fever_cycle',
            field=models.CharField(choices=[('N', 'Once in a while'), ('S', 'Very Often'), ('NN', "Don't remember the last time I got")], default=None, max_length=3, null=True, verbose_name='How often do you get cold or fever?'),
        ),
    ]
