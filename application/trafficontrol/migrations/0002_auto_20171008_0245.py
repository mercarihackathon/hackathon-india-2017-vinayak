# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trafficontrol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crossings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loc_lat', models.FloatField(verbose_name=b'Latitude')),
                ('loc_long', models.FloatField(verbose_name=b'Longitude')),
            ],
        ),
        migrations.RemoveField(
            model_name='charges',
            name='charge_kind',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='charges_due',
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.FloatField(default=0, verbose_name=b'Amount Paid'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='road_charge',
            field=models.IntegerField(default=0, verbose_name=b'Road Charges Dues'),
        ),
        migrations.AlterField(
            model_name='charges',
            name='charge',
            field=models.CharField(max_length=2, verbose_name=b'Charging nature', choices=[(b'TC', b'Toll Charge'), (b'TV', b'Traffic Light Violation'), (b'OS', b'Overspeeding')]),
        ),
        migrations.AlterField(
            model_name='missing',
            name='when',
            field=models.DateTimeField(verbose_name=b'Date of Missing Report'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_mode',
            field=models.CharField(max_length=2, verbose_name=b'Mode of Payment', choices=[(b'CA', b'Cash'), (b'NB', b'Net Banking'), (b'OW', b'Online Wallet')]),
        ),
    ]
