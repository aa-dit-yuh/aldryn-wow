# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):

    def to_settings(self, cleaned_data, settings_dict):
        return settings_dict
