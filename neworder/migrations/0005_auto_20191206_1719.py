# Generated by Django 2.1.7 on 2019-12-06 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neworder', '0004_auto_20191206_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='returned_vessel',
            field=models.BooleanField(default=False),
        ),
    ]
