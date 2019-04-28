FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY /lenta-vue-front .

RUN npm install

EXPOSE 8080

CMD [ "http-server", "dist" ]