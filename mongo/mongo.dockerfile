FROM mongo

COPY insert.py /docker-entrypoint-initdb.d/
COPY requirements.txt /tmp/requirements.txt

RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && python3 -m pip install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt


ENV MONGO_INITDB_ROOT_USERNAME=user
ENV MONGO_INITDB_ROOT_PASSWORD=password

EXPOSE 27017

CMD ["python3", "/docker-entrypoint-initdb.d/setup_mongo.py"]
