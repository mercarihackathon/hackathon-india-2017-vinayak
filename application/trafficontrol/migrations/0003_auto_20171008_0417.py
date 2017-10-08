# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trafficontrol', '0002_auto_20171008_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charges',
            name='veh_number',
            field=models.ForeignKey(verbose_name=b'Vehicle Registration Number', to='trafficontrol.Vehicle'),
        ),
        migrations.AlterField(
            model_name='missing',
            name='veh_number',
            field=models.ForeignKey(verbose_name=b'Vehicle Registration Number', to='trafficontrol.Vehicle'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='veh_number',
            field=models.ForeignKey(verbose_name=b'Vehicle Registration Number', to='trafficontrol.Vehicle'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='veh_number',
            field=models.CharField(max_length=10, serialize=False, verbose_name=b'Vehicle Registration Number', primary_key=True),
        ),
    ]
