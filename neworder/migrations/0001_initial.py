# Generated by Django 2.2 on 2020-01-20 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.TextField()),
                ('name', models.TextField()),
                ('phone_number', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=200)),
                ('tamil_name', models.TextField(blank=True, null=True)),
                ('name', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=200)),
                ('tamil_name', models.TextField(blank=True, null=True)),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vessels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.TextField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neworder.Items')),
                ('subitems', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neworder.SubItems')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.TextField()),
                ('advance', models.IntegerField()),
                ('session', models.TextField()),
                ('total', models.IntegerField()),
                ('paid_amount', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
                ('returned_vessel', models.BooleanField(default=False)),
                ('balance', models.IntegerField()),
                ('date_placed', models.DateField(auto_now_add=True)),
                ('date_of_delivery', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='neworder.CustomerDetails')),
                ('ordered_items', models.ManyToManyField(to='neworder.OrderItem')),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='subitems',
            field=models.ManyToManyField(to='neworder.SubItems'),
        ),
    ]
