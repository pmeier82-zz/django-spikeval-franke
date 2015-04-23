# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djspikeval', '0002_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultFranke',
            fields=[
                ('result_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='djspikeval.Result')),
                ('unit_gt', models.CharField(max_length=255)),
                ('unit_an', models.CharField(max_length=255)),
                ('KS', models.IntegerField(default=0)),
                ('KSO', models.IntegerField(default=0)),
                ('FS', models.IntegerField(default=0)),
                ('TP', models.IntegerField(default=0)),
                ('TPO', models.IntegerField(default=0)),
                ('FPA', models.IntegerField(default=0)),
                ('FPAE', models.IntegerField(default=0)),
                ('FPAO', models.IntegerField(default=0)),
                ('FPAOE', models.IntegerField(default=0)),
                ('FN', models.IntegerField(default=0)),
                ('FNO', models.IntegerField(default=0)),
                ('FP', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=('djspikeval.result',),
        ),
    ]
