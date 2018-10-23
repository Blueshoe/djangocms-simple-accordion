# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccordionContainer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='content_plugins_accordioncontainer', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AccordionTab',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='content_plugins_accordiontab', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default='', max_length=200, verbose_name='title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
