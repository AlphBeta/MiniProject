# Generated by Django 2.2 on 2021-03-25 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_auto_20210325_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medinfo',
            name='eye_sight',
            field=models.CharField(choices=[('Presbyopia', 'Difficulty in both'), ('Glasses', 'I wear Glasses'), ('Normal', 'I can see clearly'), ('Hypermetropia', 'Difficult in reading'), ('Myopia', 'Difficult to see distant objects')], default=False, max_length=20, verbose_name='How is your eye sight?'),
        ),
        migrations.AlterField(
            model_name='medinfo',
            name='whr',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
    ]