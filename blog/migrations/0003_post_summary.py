# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-11 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]