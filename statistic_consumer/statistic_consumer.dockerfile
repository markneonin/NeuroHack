FROM python:3.11-slim-buster

WORKDIR /statistic_consumer

COPY requirements.txt /statistic_consumer
RUN pip3 install -r requirements.txt

ADD . /statistic_consumer

CMD ["/bin/bash", "-c", "python3 ./setup_mongo.py; python3 ./app/statistic_consumer.py"]