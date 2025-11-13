from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,async_scoped_session

from Core import core_config
from asyncio import current_task


class DB:
    def __init__(self):
        self.engine = create_async_engine(
            url=core_config.db.url,
            echo=core_config.db.echo
        )

        self.session_maker = async_sessionmaker(
            bind=self.engine,
            autoflush=core_config.db.autoflush,
            expire_on_commit=core_config.db.expire_on_commit
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_maker,
            scopefunc=current_task
        )

        return session

    async def close(self):
        await  self.engine.dispose()

    async def session_dependency(self):
        session = self.get_scoped_session()

        async with session() as sess:
            yield sess

            await session.remove()

db_helper = DB()