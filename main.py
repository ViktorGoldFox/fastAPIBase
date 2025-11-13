from fastapi import FastAPI
import uvicorn

from App.endpoints import products

from contextlib import asynccontextmanager

from Core import core_config
from DataBase import db_helper, models


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

    print("uvicorn is starting...")

    yield

    print("uvicorn is stopping...")

main_app = FastAPI(lifespan=lifespan)
main_app.include_router(products, prefix='/api', tags=['Products'])

@main_app.get('/ping', tags=['Main'])
def get_ping():
    return {"code": 200, "ping": True}

if __name__ == '__main__':
    uvicorn.run('main:main_app',
                reload=core_config.api.reload,
                host=core_config.api.host,
                port=core_config.api.port)
