from django import template
from django.template.loader import render_to_string
from django.db.models.functions import Lower
from django.conf import settings

register = template.Library()


def has_visibility(user):
    visibility_groups = getattr(settings, "WAGTAIL_ACCESSIBILITY_GROUPS", [])
    if not visibility_groups:
        #  Show overlay for all users if groups have not been
        #  configured in settings
        return True
    groups = list(user.groups.values_list(Lower("name"), flat=True))
    if set(groups) & set(visibility_groups):
        return True
    return False


@register.simple_tag(takes_context=True)
def tota11y(context, override=False):
    request = context["request"]
    if has_visibility(request.user):
        if override or getattr(request, "is_preview", False):
            return render_to_string("wagtailaccessibility/tota11y.html")
    return ""
