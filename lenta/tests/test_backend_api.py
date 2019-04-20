import datetime as dt
import pytz
import pytest

from django_dynamic_fixture import G

from lenta.models import NewsPost


@pytest.mark.django_db
def test_view_news_list(client):
    G(NewsPost,
      url='1',
      original_date=dt.datetime(2019, 1, 1, tzinfo=pytz.utc),
      post_date=dt.datetime(2019, 1, 1, tzinfo=pytz.utc),
      )
    G(NewsPost,
      url='2',
      original_date=dt.datetime(2019, 2, 2, tzinfo=pytz.utc),
      post_date=dt.datetime(2019, 2, 2, tzinfo=pytz.utc),
      )

    resp = client.get('http://127.0.0.1:8000/lenta/')

    response_urls_list = [b['url'] for b in resp.json()['data']['results']]

    assert resp.status_code == 200
    assert len(response_urls_list) == 2, 'should return 2 news posts'
    assert response_urls_list == ['2', '1'], 'should return in -post_date order'


@pytest.mark.django_db
def test_view_news_post(client):
    G(NewsPost,
      url='1',
      original_date=dt.datetime(2019, 1, 1, tzinfo=pytz.utc),
      post_date=dt.datetime(2019, 1, 1, tzinfo=pytz.utc),
      )

    resp = client.get('http://127.0.0.1:8000/post/1/')
    assert resp.status_code == 200
