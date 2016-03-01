# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='dept_name',
            field=models.CharField(unique=True, max_length=40),
        ),
        migrations.AlterUniqueTogether(
            name='dept_emp',
            unique_together=set([('emp_no', 'dept_no')]),
        ),
        migrations.AlterUniqueTogether(
            name='dept_manager',
            unique_together=set([('emp_no', 'dept_no')]),
        ),
    ]
