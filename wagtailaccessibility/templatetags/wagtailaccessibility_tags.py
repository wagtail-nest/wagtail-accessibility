from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def tota11y(context):
    request = context['request']
    if getattr(request, 'is_preview', False):
        return render_to_string('wagtailaccessibility/tota11y.html')
    else:
        return ""
