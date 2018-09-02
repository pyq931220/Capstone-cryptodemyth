# Generated by Django 2.0.2 on 2018-06-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bitstamp_BTC_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('low', models.DecimalField(decimal_places=3, max_digits=10)),
                ('high', models.DecimalField(decimal_places=3, max_digits=10)),
                ('open', models.DecimalField(decimal_places=3, max_digits=10)),
                ('close', models.DecimalField(decimal_places=3, max_digits=10)),
                ('volume', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'db_table': 'data_Bitstamp_BTC_history',
            },
        ),
        migrations.CreateModel(
            name='Bitstamp_ETH_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('low', models.DecimalField(decimal_places=3, max_digits=10)),
                ('high', models.DecimalField(decimal_places=3, max_digits=10)),
                ('open', models.DecimalField(decimal_places=3, max_digits=10)),
                ('close', models.DecimalField(decimal_places=3, max_digits=10)),
                ('volume', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'db_table': 'data_Bitstamp_ETH_history',
            },
        ),
        migrations.CreateModel(
            name='Bitstamp_LTC_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('low', models.DecimalField(decimal_places=3, max_digits=10)),
                ('high', models.DecimalField(decimal_places=3, max_digits=10)),
                ('open', models.DecimalField(decimal_places=3, max_digits=10)),
                ('close', models.DecimalField(decimal_places=3, max_digits=10)),
                ('volume', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'db_table': 'data_Bitstamp_LTC_history',
            },
        ),
        migrations.CreateModel(
            name='GDAX_BTC_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('low', models.DecimalField(decimal_places=3, max_digits=10)),
                ('high', models.DecimalField(decimal_places=3, max_digits=10)),
                ('open', models.DecimalField(decimal_places=3, max_digits=10)),
                ('close', models.DecimalField(decimal_places=3, max_digits=10)),
                ('volume', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'db_table': 'data_GDAX_BTC_history',
            },
        ),
        migrations.CreateModel(
            name='GDAX_ETH_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('low', models.DecimalField(decimal_places=3, max_digits=10)),
                ('high', models.DecimalField(decimal_places=3, max_digits=10)),
                ('open', models.DecimalField(decimal_places=3, max_digits=10)),
                ('close', models.DecimalField(decimal_places=3, max_digits=10)),
                ('volume', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'db_table': 'data_GDAX_ETH_history',
            },
        ),
        migrations.CreateModel(
            name='GDAX_LTC_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('low', models.DecimalField(decimal_places=3, max_digits=10)),
                ('high', models.DecimalField(decimal_places=3, max_digits=10)),
                ('open', models.DecimalField(decimal_places=3, max_digits=10)),
                ('close', models.DecimalField(decimal_places=3, max_digits=10)),
                ('volume', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'db_table': 'data_GDAX_LTC_history',
            },
        ),
        migrations.CreateModel(
            name='latestPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
            options={
                'db_table': 'data_latest_trading_price',
            },
        ),
        migrations.CreateModel(
            name='priceChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_title', models.CharField(max_length=20)),
                ('p_shape', models.CharField(max_length=20)),
                ('p_time_unit', models.CharField(max_length=20)),
                ('p_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('p_Time', models.DateTimeField()),
                ('p_highest', models.DecimalField(decimal_places=2, max_digits=19)),
                ('p_lowest', models.DecimalField(decimal_places=2, max_digits=19)),
                ('p_volume', models.IntegerField()),
                ('p_open', models.DecimalField(decimal_places=2, max_digits=19)),
                ('p_close', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
            options={
                'db_table': 'data_price_chart',
            },
        ),
    ]
