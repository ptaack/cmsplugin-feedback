# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackplugin',
            name='email',
            field=models.EmailField(max_length=75, null=True, verbose_name='Email', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedbackplugin',
            name='form_type',
            field=models.CharField(default=b'E', max_length=1, verbose_name='Type', choices=[(b'E', 'Email'), (b'P', 'Phone')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Phone'),
            preserve_default=True,
        ),
    ]
