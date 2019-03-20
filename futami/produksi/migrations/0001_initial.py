# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-14 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='release',
            fields=[
                ('produksi_id', models.AutoField(primary_key=True, serialize=False)),
                ('nomor_palet', models.IntegerField()),
                ('jumlah_dus', models.IntegerField()),
                ('jumlah_botol', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('lokasi_penyimpanan_gudang', models.CharField(max_length=10)),
            ],
        ),
    ]
