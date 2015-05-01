# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import patterns, url

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class AnimationPlugin(CMSPluginBase):
    model = models.Animation
    name = _('Animation')
    render_template = 'aldryn_wow/animation.html'
    allow_children = True
    cache = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(AnimationPlugin)


class RevealAnimationPlugin(CMSPluginBase):
    model = models.RevealAnimation
    name = _("Wow Animation")
    render_template = 'aldryn_wow/reveal_animation.html'
    allow_children = True
    cache = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(RevealAnimationPlugin)
