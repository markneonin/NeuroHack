# from app.db.models import PostDB, OID
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

    async def _load_exgauster_components(self, exgauster):
        result = {}

        for atr, value in exgauster.items():

            if isinstance(value, dict):
                result[atr] = await self._load_latest(atr, {'component_id': value['_id']})

            elif isinstance(value, list):
                for comp in value:
                    collection = atr.replace('s_', '_')
                    result.setdefault(atr, []).append(
                        await self._load_latest(collection, {'component_id': comp['_id']})
                    )

            else:
                result[atr] = value

        return result

    async def get_exgausters(self):  # -> List[PostDB]:
        exgausters = []
        exgausters_q = self.db.exgauster.find()
        async for exgauster in exgausters_q:
            exgauster = await self._load_exgauster_components(exgauster)
            exgausters.append(exgauster)
        return exgausters

    # async def get_post(self, post_id: OID) -> PostDB:
    #     post_q = await self.db.posts.find_one({'_id': ObjectId(post_id)})
    #     if post_q:
    #         return PostDB(**post_q, id=post_q['_id'])
    #
    # async def delete_post(self, post_id: OID):
    #     await self.db.posts.delete_one({'_id': ObjectId(post_id)})
    #
    # async def update_post(self, post_id: OID, post: PostDB):
    #     await self.db.posts.update_one({'_id': ObjectId(post_id)},
    #                                    {'$set': post.dict(exclude={'id'})})
    #
    # async def add_post(self, post: PostDB):
    #     await self.db.posts.insert_one(post.dict(exclude={'id'}))


db = MongoManager()
