# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_feedback', '0003_auto_20200516_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackplugin',
            name='form_type',
            field=models.CharField(choices=[('E', 'Email'), ('P', 'Phone')], default='E', verbose_name='Type', max_length=1),
        ),
    ]
