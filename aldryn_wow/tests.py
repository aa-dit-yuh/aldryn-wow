# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase

from cms import api
from cms.models import CMSPlugin
from cms.test_utils.testcases import BaseCMSTestCase, URL_CMS_PLUGIN_ADD
from cms.utils import get_cms_setting

from .cms_plugins import AnimationPlugin, RevealAnimationPlugin


class AnimatePluginTestCase(TestCase, BaseCMSTestCase):
    su_username = 'user'
    su_password = 'pass'

    def setUp(self):
        self.template = get_cms_setting('TEMPLATES')[0][0]
        self.language = settings.LANGUAGES[0][0]
        self.page = api.create_page(
            'page',
            self.template,
            self.language,
            published=True
        )
        self.placeholder = self.page.placeholders.all()[0]
        self.superuser = self.create_superuser()

    def create_superuser(self):
        return User.objects.create_superuser(
            self.su_username,
            'email@example.com',
            self.su_password
        )

    def test_animation_simple(self):
        self.client.login(username=self.su_username, password=self.su_password)

        plugin = api.add_plugin(
            self.placeholder,
            AnimationPlugin,
            self.language,
            animation_class='fadeInDown',
        )
        self.page.publish(self.language)
        url = self.page.get_absolute_url()
        response = self.client.get(url)

        self.assertContains(response, 'animate')
        self.assertEqual(plugin.__str__(), 'fadeInDown')

    def test_animation_infinite(self):
        self.client.login(username=self.su_username, password=self.su_password)

        plugin = api.add_plugin(
            self.placeholder,
            AnimationPlugin,
            self.language,
            animation_class='bounce',
            infinite=True,
        )
        self.page.publish(self.language)
        url = self.page.get_absolute_url()
        response = self.client.get(url)

        self.assertContains(response, 'animate')
        self.assertContains(response, 'bounce')
        self.assertContains(response, 'infinite')

    def test_wow_animation_simple(self):
        self.client.login(username=self.su_username, password=self.su_password)

        plugin = api.add_plugin(
            self.placeholder,
            RevealAnimationPlugin,
            self.language,
            animation_class='bounce',
        )
        self.page.publish(self.language)
        url = self.page.get_absolute_url()
        response = self.client.get(url)
        self.assertContains(response, 'wow')
        self.assertEqual(plugin.__str__(), 'wow bounce')

    def test_wow_animation_all(self):
        self.client.login(username=self.su_username, password=self.su_password)

        plugin = api.add_plugin(
            self.placeholder,
            RevealAnimationPlugin,
            self.language,
            animation_class='fadeInLeft',
            duration=1,
            delay=2,
            offset=3,
            iteration=4
        )
        self.page.publish(self.language)
        url = self.page.get_absolute_url()
        response = self.client.get(url)

        self.assertContains(response, 'wow')
        self.assertContains(response, 'fadeInLeft')
        self.assertContains(response, 'data-wow-duration="1s"')
        self.assertContains(response, 'data-wow-delay="2s"')
        self.assertContains(response, 'data-wow-offset="3"')
        self.assertContains(response, 'data-wow-iteration="4"')
