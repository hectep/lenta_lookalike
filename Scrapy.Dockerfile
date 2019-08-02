FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY /lenta_parser/ /code/
COPY /backend/requirements.txt /code/
RUN pip install -r requirements.txt
EXPOSE 6800
STOPSIGNAL SIGINT