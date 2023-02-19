FROM python:3.11-slim-buster

WORKDIR /predict_fail

COPY requirements.txt /predict_fail
RUN pip3 install -r requirements.txt

ADD . /predict_fail


#Install Cron
RUN apt-get update
RUN apt-get -y install cron

# Add the cron job
RUN crontab -l | { cat; echo "*/10 * * * *  python3 ./app/predict_fail.py"; } | crontab -

# Run the command on container startup
CMD cron
