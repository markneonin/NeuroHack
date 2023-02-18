FROM python:3.11-slim-buster

WORKDIR /statistic_consumer

COPY requirements.txt /predict_fail
RUN pip3 install -r requirements.txt

ADD . /statistic_consumer

CMD ["python3", "./app/statistic_consumer.py"]