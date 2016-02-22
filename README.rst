=====================
wagtail-accessibility
=====================

A plugin to assist with accessibility when developing in Wagtail.

Installing
==========

Install using pip::

    pip install wagtail-accessibility

It works with Wagtail 1.0 and upwards.

Using
=====

This plugin, when added to your template, will add `tota11y <https://github.com/Khan/tota11y>`_ to all page previews. Tota11y is an accessibility visualization toolkit.

To use it, simply include this in your template, and from now on all page previews will include it.


.. code-block:: html

    {% load wagtailaccessibility_tags %}
    {% tota11y %}
