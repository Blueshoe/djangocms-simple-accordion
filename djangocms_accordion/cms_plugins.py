# -*- coding: utf-8 -*-
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase

from .models import AccordionContainer, AccordionTab


class AccordionContainerPlugin(CMSPluginBase):
    model = AccordionContainer
    name = _('Accordion')
    render_template = 'djangocms_accordion/accordion_container.html'
    allow_children = True
    child_classes = ['AccordionTabPlugin']

    def render(self, context, instance, placeholder):
        context.update({
            'accordion': instance,
            'placeholder': placeholder,
        })
        return context


class AccordionTabPlugin(CMSPluginBase):
    model = AccordionTab
    name = _('Accordion Tab')
    render_template = 'djangocms_accordion/accordion_tab.html'
    allow_children = True
    parent_classes = ['AccordionContainerPlugin']
    require_parent = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(AccordionContainerPlugin)
plugin_pool.register_plugin(AccordionTabPlugin)
