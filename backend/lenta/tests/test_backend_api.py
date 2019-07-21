import datetime as dt
import pytz
import pytest

from django_dynamic_fixture import G

from lenta.models import NewsPost, NewsLink


@pytest.mark.django_db
def test_get_news_list(client):
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

    resp = client.get('/lenta/')

    response_urls_list = [b['url'] for b in resp.json()['data']['results']]

    assert resp.status_code == 200, 'should return 200'
    assert len(response_urls_list) == 2, 'should return 2 news posts'
    assert response_urls_list == ['2', '1'], 'should return in -post_date order'


@pytest.mark.django_db
def test_get_news_post(client):
    G(NewsPost,
      url='1',
      original_date=dt.datetime(2019, 1, 1, tzinfo=pytz.utc),
      post_date=dt.datetime(2019, 1, 1, tzinfo=pytz.utc),
      )

    resp = client.get('/post/1/')
    assert resp.status_code == 200, 'should return 200'


@pytest.mark.django_db
def test_post_newspost(client):
    # request without image
    resp = client.post(
        '/lenta/',
        {
            'url': 'test_url',
            'header': 'test_header',
            'body': 'test_body',
            'original_date': dt.datetime(2019, 2, 2, tzinfo=pytz.utc),
            'post_date': dt.datetime.now(),
         }
    )

    assert resp.status_code == 201, 'should return 201'
    assert 'default_news_image.jpg' in resp.data['image'], 'there should be a default image for news without one'  # noqa


@pytest.mark.django_db
def test_get_news_links(client):
    G(NewsLink,
      url='not_valid1',
      is_parsed=True
      )
    G(NewsLink,
      url='/news/valid',
      is_parsed=False
      )
    G(NewsLink,
      url='/news/not_valid',
      is_parsed=True
      )
    G(NewsLink,
      url='not_valid2',
      is_parsed=False
      )

    resp = client.get('/links/')
    response_urls_list = [b['url'] for b in resp.json()['data']]

    assert resp.status_code == 200, 'should return 200'
    assert len(response_urls_list) == 1, 'should return only links starting with "/news" and not yet parsed'  # noqa
    assert response_urls_list == ['/news/valid'], 'should return only links starting with "/news" and not yet parsed'  # noqa


@pytest.mark.django_db
def test_create_newslink(client):
    resp = client.post('/links/', {'url': 'test_url'})

    assert resp.status_code == 201, 'should return 201'

    # trying to create link with the same url
    resp = client.post('/links/', {'url': 'test_url'})
    assert resp.status_code == 400, 'should return 400'


@pytest.mark.django_db
def test_update_newslink(client):
    news_link = G(
        NewsLink,
        url='/news/valid',
        is_parsed=False)

    url_to_news_link = f'/links/{news_link.pk}/'
    resp = client.post(url_to_news_link, {'is_parsed': 'true'})

    assert resp.status_code == 200, 'should return 200'


