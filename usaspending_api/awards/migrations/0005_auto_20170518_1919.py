# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-18 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_auto_20170515_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaltransactionassistance',
            name='cfda_number',
        ),
        migrations.RemoveField(
            model_name='historicaltransactionassistance',
            name='cfda_title',
        ),
        migrations.RemoveField(
            model_name='transactionassistance',
            name='cfda_number',
        ),
        migrations.RemoveField(
            model_name='transactionassistance',
            name='cfda_title',
        ),
    ]