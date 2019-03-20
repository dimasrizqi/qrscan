# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 04:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0004_auto_20190320_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='transisi',
            fields=[
                ('transisi_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_perpindahan', models.CharField(choices=[('CONVEYOR', 'CONVEYOR'), ('GUDANG TRANSISI', 'GUDANG TRANSISI'), ('GUDANG RACKING', 'GUDANG RACKING')], max_length=100)),
                ('product_per_palet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produksi.productperpalet')),
            ],
        ),
    ]
