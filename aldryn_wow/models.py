# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from cms.models.pluginmodel import CMSPlugin

from .constants import ANIMATION_CHOICES


@python_2_unicode_compatible
class Animation(CMSPlugin):
    animation_class = models.CharField(
        max_length=25,
        choices=ANIMATION_CHOICES,
        default=ANIMATION_CHOICES[0][0],
        blank=False,
    )
    infinite = models.NullBooleanField(
        help_text=_('Infinite Loop'),
    )

    def __str__(self):
        return _(self.animation_class)


@python_2_unicode_compatible
class RevealAnimation(CMSPlugin):
    animation_class = models.CharField(
        max_length=25,
        choices=ANIMATION_CHOICES,
        default=ANIMATION_CHOICES[0][0],
        blank=False,
    )
    duration = models.PositiveSmallIntegerField(
        help_text=_('Change the animation duration'),
        null=True
    )
    delay = models.PositiveSmallIntegerField(
        help_text=_('Delay before the animation starts'),
        null=True,
    )
    offset = models.PositiveSmallIntegerField(
        help_text=_(
            'Distance to start the animation '
            '(related to the browser bottom)'
        ),
        null=True,
    )
    iteration = models.PositiveSmallIntegerField(
        help_text=_('Number of times the animation is repeated'),
        null=True,
    )

    def __str__(self):
        return ''.join(('wow ', self.animation_class))
