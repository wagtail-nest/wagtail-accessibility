from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def tota11y(context, override=False):
    request = context['request']
    if override or getattr(request, 'is_preview', False):
        return render_to_string('wagtailaccessibility/tota11y.html')
    else:
        return ""
