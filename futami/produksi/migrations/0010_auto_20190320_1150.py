# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 04:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0009_auto_20190320_1150'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='gudangracking',
        #     fields=[
        #         ('gudangracking_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('blok', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')], max_length=10)),
        #         ('tingkat', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10)),
        #         ('lorong', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30')], max_length=10)),
        #         ('baris', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='product',
        #     fields=[
        #         ('id_product', models.AutoField(primary_key=True, serialize=False)),
        #         ('nama_product', models.CharField(max_length=100)),
        #         ('varian', models.CharField(max_length=100)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='productkeluar',
        #     fields=[
        #         ('productkeluar_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('list_product', models.CharField(max_length=500)),
        #         ('nomor_segel', models.CharField(max_length=20)),
        #         ('referensi_qc', models.CharField(choices=[('OK', 'OK'), ('NOT OK', 'NOT OK')], max_length=10)),
        #         ('nomor_do', models.CharField(max_length=20)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='productperpalet',
        #     fields=[
        #         ('productperpalet_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('tanggal_produksi', models.DateField()),
        #         ('jumlah_dus', models.IntegerField()),
        #         ('jumlah_botol', models.IntegerField()),
        #         ('status', models.CharField(max_length=10)),
        #         ('nama_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produksi.product')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='transisi',
        #     fields=[
        #         ('transisi_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('status_perpindahan', models.CharField(choices=[('CONVEYOR', 'CONVEYOR'), ('GUDANG TRANSISI', 'GUDANG TRANSISI'), ('GUDANG RACKING', 'GUDANG RACKING')], max_length=100)),
        #         ('product_per_palet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produksi.productperpalet')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='tujuan',
        #     fields=[
        #         ('tujuan_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('nama_tujuan', models.CharField(max_length=200)),
        #         ('alamat_tujuan', models.CharField(max_length=500)),
        #     ],
        # ),
        # migrations.AddField(
        #     model_name='productkeluar',
        #     name='tujuan',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produksi.tujuan'),
        # ),
        # migrations.AddField(
        #     model_name='gudangracking',
        #     name='product_per_palet',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produksi.productperpalet'),
        # ),
    ]
