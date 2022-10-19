try:
    from wagtail.models import Page
except ImportError:
    # Wagtail<3.0
    from wagtail.core.models import Page


class SimplePage(Page):
    pass
