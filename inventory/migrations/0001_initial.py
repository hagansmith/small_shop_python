# Generated by Django 2.1.1 on 2018-09-09 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255)),
                ('closed_at', models.DateTimeField(verbose_name='date closed')),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('updated_at', models.DateTimeField(verbose_name='date updated')),
                ('number', models.IntegerField()),
                ('note', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('gateway', models.GenericIPAddressField()),
                ('test', models.BooleanField()),
                ('total_price', models.FloatField()),
                ('subtotal_price', models.FloatField()),
                ('total_weight', models.FloatField()),
                ('total_tax', models.FloatField()),
            ],
        ),
    ]
