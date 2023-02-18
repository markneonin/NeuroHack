import asyncio
import datetime
import json
import os
import ssl
from pathlib import Path

import motor.motor_asyncio
from aiokafka import AIOKafkaConsumer
from dotenv import load_dotenv

from signals_mapping import signals_mapping

dotenv_path = Path('./constants/.env')
load_dotenv(dotenv_path=dotenv_path)

STATISTIC_DB = os.getenv('STATISTIC_DB')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_HOST')
KAFKA_CONSUMER_GROUP = os.getenv('KAFKA_CONSUMER_GROUP')
USERNAME = os.getenv('KAFKA_USERNAME')
PASSWORD = os.getenv('KAFKA_PASSWORD')

SASL_MECHANISM = os.getenv('KAFKA_SASL_MECHANISM')
SASL_SSL = os.getenv('KAFKA_SASL_SSL')

SSL_CONTEXT = ssl.create_default_context(cafile='./constants/CA.pem')

client = motor.motor_asyncio.AsyncIOMotorClient(STATISTIC_DB, serverSelectionTimeoutMS=5000)
db = client.statistic

offset = '32958'


def parse_signals(msg):
    timestamp = datetime.datetime.fromisoformat(msg.pop('moment'))
    signals = [
        {
            'key': code,
            'exgauster': signals_mapping.get(code).get('exgauster'),
            'moment': timestamp,
            'value': value,
        }
        for code, value in msg.items()
    ]
    return signals


async def write_to_mongo(signals):
    await db.signal.insert_many(signals)


async def handle_message(msg: bytes):
    msg = json.loads(msg.decode())
    signals = parse_signals(msg)
    # await write_to_mongo(signals)


async def consume():
    consumer = AIOKafkaConsumer(KAFKA_TOPIC,
                                bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                                sasl_plain_password=PASSWORD,
                                sasl_plain_username=USERNAME,
                                sasl_mechanism=SASL_MECHANISM,
                                group_id=KAFKA_CONSUMER_GROUP,
                                ssl_context=SSL_CONTEXT,
                                security_protocol=SASL_SSL,
                                enable_auto_commit=False,
                                auto_offset_reset=offset,

                                )
    await consumer.start()

    try:
        async with asyncio.TaskGroup() as tg:
            async for msg in consumer:
                print(msg.value.decode())
                break
                tg.create_task(handle_message(msg.value))

    finally:
        await consumer.stop()


if __name__ == '__main__':
    print(signals_mapping)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume())
