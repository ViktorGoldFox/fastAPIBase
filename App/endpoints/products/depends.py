from fastapi import HTTPException, Body
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from DataBase.models import Products
from DataBase import db_helper

async def is_existence_product(
        product_id: int = Body(...),
        session: AsyncSession = Depends(db_helper.session_dependency)
) -> int | HTTPException:
    stmt = select(Products).where(Products.id == product_id)

    result: Result = await session.execute(stmt)
    product = result.scalars().first()

    if product:
        return product.id
    else:
        raise HTTPException(status_code=404, detail="Product not found")
