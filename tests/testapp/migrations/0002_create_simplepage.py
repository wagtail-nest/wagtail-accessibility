# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def create_simplepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    SimplePage = apps.get_model('testapp.SimplePage')

    # Delete the default simplepage
    # If migration is run multiple times, it may have already been deleted
    Page.objects.filter(id=2).delete()

    # Create content type for simplepage model
    simplepage_content_type, __ = ContentType.objects.get_or_create(
        model='simplepage', app_label='testapp')

    # Create a new simplepage
    simplepage = SimplePage.objects.create(
        title="Home",
        draft_title="Home",
        slug='testapp',
        content_type=simplepage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/testapp/',
    )

    # Create a site with the new simplepage set as the root
    Site.objects.create(
        hostname='localhost', root_page=simplepage, is_default_site=True)


def remove_simplepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    SimplePage = apps.get_model('testapp.SimplePage')

    # Delete the default simplepage
    # Page and Site objects CASCADE
    SimplePage.objects.filter(slug='testapp', depth=2).delete()

    # Delete content type for simplepage model
    ContentType.objects.filter(model='simplepage', app_label='testapp').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_simplepage, remove_simplepage),
    ]
