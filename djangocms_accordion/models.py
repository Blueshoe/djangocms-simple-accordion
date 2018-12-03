# -*- coding: utf-8 -*-
from cms.models import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class AccordionContainer(CMSPlugin):
    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return _(u'%s columns') % self.cmsplugin_set.all().count()


@python_2_unicode_compatible
class AccordionTab(CMSPlugin):
    title = models.CharField(_('title'), max_length=200, default=u'')

    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
