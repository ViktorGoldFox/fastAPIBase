from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from DataBase import db_helper
from App.endpoints.products import crud, depends
from Core import schemes

products_router = APIRouter()


@products_router.get("/products", response_model=List[schemes.Product])
async def get_products(
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    db_answer = await crud.get_all_products(session)

    return db_answer


@products_router.post("/products", response_model=schemes.Product)
async def post_products(
    new_product: schemes.NewProduct,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    created_product = await crud.add_new_product(session, new_product)

    return created_product


@products_router.delete("/products")
async def delete_products(
    delete_id: int = Depends(depends.is_existence_product),
    session: AsyncSession = Depends(db_helper.session_dependency)
):

    await crud.delete_product(session, delete_id)
