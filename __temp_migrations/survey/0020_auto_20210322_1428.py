# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2021-03-22 19:28
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0019_auto_20210322_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='risk',
            field=otree.db.models.StringField(choices=[('0 risk averse', '0 risk averse'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10 fully prepared to take risks', '10 fully prepared to take risks')], max_length=10000, null=True, verbose_name='귀하는 자신을 개인적으로 어떻게 평가하십니까? 일반적으로 기꺼이 위험을 감수하는 사람입니까, 아니면 위험을 피하려고 합니까? 제공된 척도를 사용하여 답변을 해 주십시오. 0은 "전혀 위험을 감수할 준비가 되어 있지 않음"을 의미합니다. 10은 "위험을 감수할 준비가 되어 있음"을 의미합니다. 귀하는 0-10 사이의 숫자를 사용하여 답변할 수 있습니다.'),
        ),
    ]
