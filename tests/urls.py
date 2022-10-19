from django.urls import include, path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

try:
    from wagtail import urls as wagtail_urls
except ImportError:
    # Wagtail<3.0
    from wagtail.core import urls as wagtail_urls


urlpatterns = [
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("", include(wagtail_urls)),
]
