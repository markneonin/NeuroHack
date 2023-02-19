from app.db.mongo import db


class ExgausterService:
    def __init__(self,):
        self.db = None

    async def get_exgausters(self):
        exgausters = await db.get_exgausters()
        return exgausters

