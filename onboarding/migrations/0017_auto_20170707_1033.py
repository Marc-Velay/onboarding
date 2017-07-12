# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-07 10:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0016_auto_20170706_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontact',
            name='dob',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.RegexValidator(message='Must be a Date', regex='^\\d{4}-\\d{2}-\\d{2}$')], verbose_name='Birthdate'),
        ),
        migrations.AlterField(
            model_name='usercontact',
            name='doe',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.RegexValidator(message='Must be a Date', regex='^\\d{4}-\\d{2}-\\d{2}$')], verbose_name='Expiracydate'),
        ),
    ]
