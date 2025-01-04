from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from app.v1 import crud

from untities import *

app_v1 = APIRouter()

@app_v1.get('/ping')
def get_ping():
    return {"code": 200, "ping": True}

@app_v1.get('/products')
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    db_answer = await crud.get_all_product(session)

    return {"code": 200, "data": db_answer}

@app_v1.post('/products')
async def post_products(new_product: Getting_product, session: AsyncSession = Depends(db_helper.session_dependency)):
    db_answer = await crud.add_new_product(session, new_product)

    return {"code": 200}

@app_v1.delete('/products')
async def delete_products(delete_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    db_answer = await crud.delete_product(session, delete_id)

    return {"code": 200}