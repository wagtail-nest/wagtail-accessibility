from django.conf import settings
from pytest_django.asserts import assertInHTML, assertJSONEqual

from tests.testapp.models import SimplePage


validity = {
    'is_valid': True
}

if settings.WAGTAIL_VERSION >= (4, 0):
    validity['is_available'] = True


def test_preview(admin_client):
    simple_page = SimplePage.objects.first()

    post_data = {
        'title': "Accessibility",
        'slug': 'accessibility',
    }

    preview_url = "/admin/pages/{}/edit/preview/".format(simple_page.pk)
    response = admin_client.post(preview_url, post_data)

    # Check the JSON response
    assert response.status_code == 200
    assertJSONEqual(response.content.decode(), validity)

    # Check the user can refresh the preview
    preview_session_key = 'wagtail-preview-{}'.format(simple_page.pk)
    assert preview_session_key in admin_client.session

    response = admin_client.get(preview_url)

    # Check the HTML response
    assert response.status_code == 200
    assertInHTML(
        '<script src="/static/js/tota11y.min.js"></script>',
        response.content.decode(),
    )
