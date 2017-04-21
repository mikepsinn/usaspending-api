# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-06 03:25
from __future__ import unicode_literals

from django.db import migrations

from usaspending_api.accounts.models import (AppropriationAccountBalancesQuarterly)


def insert_quarterly_records(apps, schema_editor):
    """Insert quarterly tas balances for existing submissions."""
    AppropriationAccountBalancesQuarterly.insert_quarterly_numbers()


def remove_quarterly_records(apps, schema_editor):
    """Delete quarterly tas balances for existing submissions."""
    AppropriationAccountBalancesQuarterly.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_appropriationaccountbalancesquarterly'),
        ('accounts', '0021_auto_20170405_1909'),  # needs to run after migration to fix signs
    ]

    operations = [
        migrations.RunPython(insert_quarterly_records, remove_quarterly_records),
    ]