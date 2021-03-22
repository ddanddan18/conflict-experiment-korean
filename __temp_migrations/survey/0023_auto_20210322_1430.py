# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2021-03-22 19:30
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0022_auto_20210322_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='intent',
            field=otree.db.models.StringField(choices=[('Selfish', 'Selfish'), ('Generous', 'Generous'), ('Hostile', 'Hostile'), ('Cooperative', 'Cooperative'), ('Rational', 'Rational'), ('Irrational', 'Irrational')], max_length=10000, null=True, verbose_name='귀하는 상대방 참가자가 결정을 할 때 어떤 의도를 지니고 있었다고 생각하십니까?'),
        ),
    ]
