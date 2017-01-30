# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OutgoingIrcMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('target', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=200)),
                ('processed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
