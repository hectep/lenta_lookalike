# lenta_lookalike

>Django-rest-framework based backend plus
> a vue.js frontend

## Build Setup

Backend:


``` bash
# install dependencies
pip install -r requirements.txt
# run at localhost:8000
python manage.py runserver
```
Frontend:

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

Celery-based file parsing:

``` bash
#start worker
celeery worker -A lenta
#start schedule
celery -A lenta beat
```

This project contains a news website, that boldly steals all its content from lenta.ru using celery and scrapy. Backend is made with Django + DRF. Frontend uses vue.js framework. 