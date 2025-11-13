from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from DataBase import db_helper
from App.endpoints.products import crud

from Schemes import *

products_router = APIRouter()

@products_router.get('/products')
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    db_answer = await crud.get_all_product(session)

    return {"code": 200, "data": db_answer}

@products_router.post('/products')
async def post_products(new_product: Getting_product, session: AsyncSession = Depends(db_helper.session_dependency)):
    db_answer = await crud.add_new_product(session, new_product)

    return {"code": 200}

@products_router.delete('/products')
async def delete_products(delete_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    db_answer = await crud.delete_product(session, delete_id)

    return {"code": 200}