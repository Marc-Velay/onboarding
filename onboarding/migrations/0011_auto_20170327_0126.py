# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0010_auto_20170325_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesnapshot',
            name='model_pic',
            field=models.ImageField(blank=True, null=True, upload_to='/home/gniorg/Documents/CIMD/website/onboarding/mainSite/media/onboarding/'),
        ),
    ]