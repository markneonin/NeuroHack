# from app.db.models import PostDB, OID
import asyncio

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoManager:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect_to_database(self, host: str):
        self.client = AsyncIOMotorClient(host)
        self.db = self.client.statistic

    async def close_database_connection(self):
        self.client.close()

    async def _load_latest(self, collection, query):
        async for e in self.db[collection].find(query).sort('moment', -1).limit(1):
            return e

    async def _load_component(self, attribute, componenet, result):
        result[attribute] = await self._load_latest(attribute, {'component_id': componenet['_id']})

    async def _load_components(self, attribute, component, result):
        collection = attribute.replace('s_', '_')
        data = await self._load_latest(collection, {'component_id': component['_id']})
        data['number'] = component['number']
        result.setdefault(attribute, []).append(data)

    async def _load_exgauster_components(self, exgauster):
        result = {}
        tasks = []
        for atr, value in exgauster.items():

            if isinstance(value, dict):
                tasks.append(asyncio.create_task(self._load_component(atr, value, result)))

            elif isinstance(value, list):
                for comp in value:
                    tasks.append(asyncio.create_task(self._load_components(atr, comp, result)))
            else:
                result[atr] = value

        await asyncio.gather(*tasks)

        return result

    async def get_exgauster(self, number):
        exgauster = await self.db.exgauster.find_one({'number': number})
        result = await self._load_exgauster_components(exgauster)
        return result

    async def get_exgausters(self):
        exgausters_q = self.db.exgauster.find()
        exgausters = await asyncio.gather(*(
            asyncio.create_task(self._load_exgauster_components(exgauster))
            for exgauster in await exgausters_q.to_list(length=100)
        ))
        return exgausters


db = MongoManager()
