# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_token_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='uid',
            field=models.CharField(default='', max_length=40),
        ),
    ]
