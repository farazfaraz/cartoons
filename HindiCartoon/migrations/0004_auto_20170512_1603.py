# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-12 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HindiCartoon', '0003_remove_cartoon_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_name', models.CharField(max_length=500)),
                ('cartoon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HindiCartoon.Cartoon')),
            ],
        ),
        migrations.RemoveField(
            model_name='episode',
            name='cartoon',
        ),
        migrations.AddField(
            model_name='episode',
            name='episode',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='HindiCartoon.Season'),
            preserve_default=False,
        ),
    ]
