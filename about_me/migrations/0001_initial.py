# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information_about_me',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('date_of_birth', models.DateTimeField()),
                ('bio', models.TextField(max_length=10000)),
                ('contacts', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('jabber', models.CharField(max_length=30)),
                ('skype', models.CharField(max_length=30)),
                ('other_contacts', models.TextField(max_length=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
