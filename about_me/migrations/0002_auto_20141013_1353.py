# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information_about_me',
            name='bio',
            field=models.TextField(max_length=10000, blank=True),
        ),
        migrations.AlterField(
            model_name='information_about_me',
            name='contacts',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='information_about_me',
            name='email',
            field=models.EmailField(max_length=75, blank=True),
        ),
        migrations.AlterField(
            model_name='information_about_me',
            name='jabber',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='information_about_me',
            name='other_contacts',
            field=models.TextField(max_length=10000, blank=True),
        ),
        migrations.AlterField(
            model_name='information_about_me',
            name='skype',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
