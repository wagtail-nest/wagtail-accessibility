from django import template
from django.conf import settings
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def tota11y(context):
    request = context['request']
    source = settings.STATIC_URL + 'tota11y.min.js'
    if request.is_preview:
        return render_to_string('wagtailaccessibility/tota11y.html', {
            'source': source,
        })
    else:
        return ""
