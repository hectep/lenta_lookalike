# lenta_lookalike

>Django-rest-framework based backend plus
> a vue.js frontend

This project contains a news website, that boldly steals all its content from lenta.ru using scrapy. Backend is made with Django + DRF. Frontend uses vue.js framework. 

## Build Setup
```
docker-compose build
docker-compose up
```
Or if you want to start it without docker:

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

News scraping:

``` bash
#start News links scraping 
curl http://localhost:6800/schedule.json -d project=default -d spider=News    
#start News posts scraping
curl http://localhost:6800/schedule.json -d project=default -d spider=NewsPost    
```