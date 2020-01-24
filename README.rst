=====================
wagtail-accessibility
=====================

A plugin to assist with accessibility when developing in Wagtail. `Screencast demo <https://www.youtube.com/watch?v=QrgTrE0ug60>`_.

Installing
==========

Install using pip::

    pip install wagtail-accessibility

Then add 'wagtailaccessibility' to your INSTALLED_APPS. It works with Wagtail 1.0 and upwards.

If you want to restrict visibility of the template tag to specific groups, add a 'WAGTAIL_ACCESSIBILITY_GROUPS' setting with a list of groups. For example::

    WAGTAIL_ACCESSIBILITY_GROUPS = ["editors", "moderators"]

Using
=====

This plugin, when added to your template, will add `tota11y <https://github.com/Khan/tota11y>`_ to all page previews. Tota11y is an accessibility visualization toolkit.

To use it, simply include this in your template, and from now on all page previews will include it.


.. code-block:: html

    {% load wagtailaccessibility_tags %}
    {% tota11y %}

Jinja2
======

This plugin also contains a jinja2 implementation, to use it, include the following in your config.

.. code-block:: python

    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'OPTIONS': {
            'extensions': [
                ...
                'wagtailaccessibility.jinja2tags.tota11y',
            ],
        },
    }

The template tag can then be used like so.

.. code-block:: html

    {{ tota11y() }}
