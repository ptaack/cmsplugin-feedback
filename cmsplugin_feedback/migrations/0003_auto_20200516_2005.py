# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_feedback', '0002_auto_20200516_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackplugin',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email', blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
