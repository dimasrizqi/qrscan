# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 04:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0003_product_produkperpalet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='produkperpalet',
            new_name='productperpalet',
        ),
        migrations.RenameField(
            model_name='productperpalet',
            old_name='produkperpalet_id',
            new_name='productperpalet_id',
        ),
    ]
