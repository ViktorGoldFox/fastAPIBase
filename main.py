from fastapi import FastAPI
import uvicorn

from app.v1.views import app_v1

from contextlib import asynccontextmanager

from core import project_setting as settings
from database import db_helper, models


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

    print("uvicorn is starting...")

    yield

    print("uvicorn is stopping...")

main_app = FastAPI(lifespan=lifespan)
main_app.include_router(app_v1, prefix='/api/v1', tags=['v1'])

if __name__ == '__main__':
    uvicorn.run('main_app:main',
                reload=settings.api.reload,
                host=settings.api.host,
                port=settings.api.port)
