from sqlalchemy import select, delete, Result, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from DataBase.models import Products
from Core import schemes


async def get_all_products(session: AsyncSession) -> Sequence[Products]:
    stmt = select(Products)

    result: Result = await session.execute(stmt)

    products = result.scalars().all()

    return products


async def add_new_product(session: AsyncSession, new_product: schemes.NewProduct) -> Products:
    product = Products(**new_product.model_dump())

    session.add(product)

    await session.commit()
    await session.refresh(product)

    return product



async def delete_product(session: AsyncSession, delete_id: int) -> None:
    stmt = delete(Products).where(Products.id == delete_id)

    await session.execute(stmt)
    await session.commit()