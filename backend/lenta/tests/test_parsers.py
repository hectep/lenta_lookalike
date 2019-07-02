import requests

from django.conf import settings


def test_lenta_connection():
    resp = requests.get(settings.LENTA_URL)
    assert resp.status_code == 200, 'link to lenta.ru is wrong'
