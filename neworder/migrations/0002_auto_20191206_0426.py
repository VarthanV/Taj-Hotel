# Generated by Django 2.1.7 on 2019-12-06 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neworder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyitems',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dailysubitems',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
