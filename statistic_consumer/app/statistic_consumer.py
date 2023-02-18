import asyncio
import datetime
import json
import os
import ssl
from pathlib import Path

import motor.motor_asyncio
from aiokafka import AIOKafkaConsumer
from dotenv import load_dotenv

from signals_mapping import prediction_keys

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

client = motor.motor_asyncio.AsyncIOMotorClient(STATISTIC_DB)
db = client.statistic

attribute_collection = {
    'bearings_big': 'bearing_big',
    'bearings_small': 'bearing_small',
    'cooler': 'cooler',
    'gas_manifold': 'gas_manifold',
    'valve_position': 'valve_position',
    'main_drive': 'main_drive',
    'oil_system': 'oil_system',
    'exgauster_work': 'exgauster_work',
}

offset = 'earliest'


def parse_component(component, msg):
    entity = {
        'component_id': component['_id'],
    }

    for field, code in component['fields_map'].items():
        entity[field] = msg.get(code)

    return entity


def parse_message(msg, exgausters):
    moment = datetime.datetime.fromisoformat(msg.pop('moment'))
    to_write = {}

    for exg in exgausters:
        for attr, collection in attribute_collection.items():

            component = exg[attr]
            if isinstance(component, list):

                for sub_component in component:
                    entity = parse_component(sub_component, msg)
                    entity.update(moment=moment)
                    to_write.setdefault(collection, []).append(entity)

            else:
                entity = parse_component(component, msg)
                entity.update(moment=moment)
                to_write.setdefault(collection, []).append(entity)

    return to_write


async def _insert_into_collection(collection, entities):
    await db[collection].insert_many(entities)


async def write_to_mongo(to_write):
    await asyncio.gather(*(
        asyncio.create_task(_insert_into_collection(collection, entities))
        for collection, entities in to_write.items()
    ))


async def handle_message(msg: bytes, exgausters):
    msg = json.loads(msg.decode())

    to_write = parse_message(msg, exgausters)
    await write_to_mongo(to_write)


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
    exgausters_cursor = db.exgauster.find()
    exgausters = [e for e in await exgausters_cursor.to_list(length=100)]
    await consumer.start()

    try:
        async with asyncio.TaskGroup() as tg:
            async for msg in consumer:
                print(msg.offset)
                tg.create_task(handle_message(msg.value, exgausters))
                tg.create_task(parse_signals(msg = json.loads(msg.value.decode())))
    finally:
        await consumer.stop()


async def parse_signals(msg):
    timestamp = datetime.datetime.fromisoformat(msg.pop('moment'))

    signals = [
        {
            'key': code,
            'moment': timestamp,
            'value': value,
        }
        for code, value in msg.items() if code in prediction_keys
    ]
    await db.signal.insert_many(signals)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume())
