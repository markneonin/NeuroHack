FROM python:3.11-slim-buster

WORKDIR /api

COPY requirements.txt /api
RUN pip3 install -r requirements.txt

ADD . /api

RUN chmod +x /api/run.sh

EXPOSE 8000

CMD ["/bin/bash", "-c", "python3 /api/setup_mongo.py; /api/run.sh"]