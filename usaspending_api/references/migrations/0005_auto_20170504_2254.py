# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-04 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0004_add_slug_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='definitionresource',
            name='definition',
        ),
        migrations.AddField(
            model_name='definition',
            name='resources',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='definition',
            name='plain',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='DefinitionResource',
        ),
    ]
