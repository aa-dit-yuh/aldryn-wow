=============
aldryn-wow
=============

.. image:: https://badge.fury.io/py/aldryn-wow.svg
    :target: http://badge.fury.io/py/aldryn-wow
.. image:: https://travis-ci.org/narayanaditya95/aldryn-wow.svg?branch=master
    :target: https://travis-ci.org/narayanaditya95/aldryn-wow
.. image:: https://coveralls.io/repos/narayanaditya95/aldryn-wow/badge.svg?branch=master
    :target: https://coveralls.io/r/narayanaditya95/aldryn-wow?branch=master
.. image:: https://landscape.io/github/narayanaditya95/aldryn-wow/master/landscape.svg?style=flat
    :target: https://landscape.io/github/narayanaditya95/aldryn-wow/master
    :alt: Code Health

------------

Plugin for django-cms to include awesome animations from `WOW <http://mynameismatthieu.com/WOW/>`_.js and `Animate <http://daneden.github.io/animate.css/>`_.css

Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`, run ``pip install aldryn-wow``
* If using Django 1.6 add ``'aldryn_wow': 'aldryn_wow.south_migrations',``
  to ``SOUTH_MIGRATION_MODULES``  (or define ``SOUTH_MIGRATION_MODULES`` if it does not exists);
* Run ``manage.py migrate aldryn_wow``


Usage
-----

Default content in Placeholder
******************************

If you use Django-CMS >= 3.0, you can use ``Animation`` and ``Wow Animation`` in "default_plugins"
(see docs about the CMS_PLACEHOLDER_CONF setting in Django CMS 3.0).

