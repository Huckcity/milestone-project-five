# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 01:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20190324_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
