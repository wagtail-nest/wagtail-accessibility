import jinja2
from jinja2.ext import Extension

from django.template.loader import render_to_string


@jinja2.contextfunction
def tota11y_include(context):
    request = context.get('request')
    if request.is_preview:
        return render_to_string('wagtailaccessibility/tota11y.html')
    else:
        return ""


class WagtailAccessibilityExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)

        self.environment.globals.update({
            'tota11y': tota11y_include,
        })

tota11y = WagtailAccessibilityExtension
