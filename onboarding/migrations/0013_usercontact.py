# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-06 13:26
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0012_auto_20170411_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('firstname', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(message='Must be an alphanumeric', regex='^[A-Za-z1-9ÑñÃãÁáÀàÂâÇçÉéÊêÍíÕõÓóÔôÚúÜü]+((\\-| )[A-Za-z1-9ÑñÃãÁáÀàÂâÇçÉéÊêÍíÕõÓóÔôÚúÜü]+)*$')], verbose_name='First Name')),
                ('lastname', models.CharField(blank=True, max_length=40, validators=[django.core.validators.RegexValidator(message='Must be an alphanumeric', regex='^[A-Za-z1-9ÑñÃãÁáÀàÂâÇçÉéÊêÍíÕõÓóÔôÚúÜü]+((\\-| )[A-Za-z1-9ÑñÃãÁáÀàÂâÇçÉéÊêÍíÕõÓóÔôÚúÜü]+)*$')], verbose_name='Last Name')),
                ('nationality', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Must be a 2-4 capital letter word', regex='^[A-Za-z]*$')], verbose_name='Nationality')),
                ('birthdate', models.DateField(blank=True, null=True, validators=[django.core.validators.RegexValidator(message='Must be a Date', regex='^[0-9]{6}$')], verbose_name='Birthdate')),
                ('expiracydate', models.DateField(blank=True, null=True, validators=[django.core.validators.RegexValidator(message='Must be a Date', regex='^[0-9]{6}$')], verbose_name='Expiracydate')),
                ('dni', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='Must be 8 numbers followed by 1 capital letter', regex='^[0-9]{8}[A-Z]{1}$')], verbose_name='DNI')),
                ('front_pic', models.ImageField(blank=True, null=True, upload_to='/home/gniorg/Documents/CIMD/website/onboarding/media/onboarding/userpictures')),
                ('back_pic', models.ImageField(blank=True, null=True, upload_to='/home/gniorg/Documents/CIMD/website/onboarding/media/onboarding/userpictures')),
            ],
        ),
    ]
