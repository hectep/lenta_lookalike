FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY /backend/ /code/
RUN pip install -r requirements.txt
# Server
EXPOSE 8000
STOPSIGNAL SIGINT