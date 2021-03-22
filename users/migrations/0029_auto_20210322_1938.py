# Generated by Django 2.2 on 2021-03-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20210322_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medinfo',
            name='fever',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Are you ill/Having Cold?'),
        ),
        migrations.AlterField(
            model_name='medinfo',
            name='fever_cycle',
            field=models.CharField(choices=[('NN', "Don't remember the last time I got"), ('N', 'Once in a while'), ('S', 'Very Often')], default=None, max_length=3, null=True, verbose_name='How often do you get cold or fever?'),
        ),
    ]