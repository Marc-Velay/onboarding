# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-06 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0015_auto_20170706_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontact',
            name='back_pic',
            field=models.ImageField(blank=True, null=True, upload_to='onboarding/userpictures/'),
        ),
        migrations.AlterField(
            model_name='usercontact',
            name='front_pic',
            field=models.ImageField(blank=True, null=True, upload_to='onboarding/userpictures/'),
        ),
    ]
