# -*- coding: utf-8 -*-
from cms.models import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class AccordionContainer(CMSPlugin):
    def __str__(self):
        return _(u'%s columns') % self.cmsplugin_set.all().count()


@python_2_unicode_compatible
class AccordionTab(CMSPlugin):
    title = models.CharField(_('title'), max_length=200, default='')

    def __str__(self):
        return self.title
