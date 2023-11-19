FROM python:3.10.12-bookworm
MAINTAINER Thomas

WORKDIR /damn

COPY requirements.txt /damn
RUN pip install -r requirements.txt
COPY ${pwd} /damn
ENTRYPOINT ["flask","--app","app.py","--no-debug","run","--host","0.0.0.0","--port","8080"]

