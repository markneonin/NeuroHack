FROM mongo


RUN apt-get update && \
    apt-get install -y gnupg python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY setup_mongo.py /insert.py
RUN python3 /insert.py


ENV MONGO_INITDB_ROOT_USERNAME=user
ENV MONGO_INITDB_ROOT_PASSWORD=password

EXPOSE 27017