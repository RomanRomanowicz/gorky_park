# Generated by Django 4.0.6 on 2022-07-04 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportingdoggies',
            name='tickets',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reportingdoggies',
            name='visitors',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
