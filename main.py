from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from Core import settings
from DataBase import db_helper, models
from App.endpoints import products_router


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

    print("Uvicorn is starting...")

    yield

    print("Uvicorn is stopping...")


app = FastAPI(lifespan=lifespan)
app.include_router(products_router, prefix="/api", tags=["products"])


@app.get("/ping", tags=["main"])
def get_ping():
    return {"ping": True}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=settings.api.reload,
        host=settings.api.host,
        port=settings.api.port,
    )
