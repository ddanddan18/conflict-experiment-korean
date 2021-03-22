# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2021-03-22 19:31
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0031_auto_20210322_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='identity',
            field=otree.db.models.StringField(choices=[('예', '예'), ('아니오', '아니오'), ('Maybe', 'Maybe')], max_length=10000, null=True, verbose_name='만약 귀하가 같이 게임을 한 상대방 참가자가 누구인지 알았다면, 다른 선택을 내렸을 것이라고 생각하십니까?'),
        ),
    ]
