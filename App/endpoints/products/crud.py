from sqlalchemy import select, delete, Result
from sqlalchemy.ext.asyncio import AsyncSession

from DataBase.models import Products
from Schemes import Product, GettingProduct


async def get_all_product(session: AsyncSession):
    stmt = select(Products)

    result: Result = await session.execute(stmt)

    objects = result.scalars().all()

    return objects


async def delete_product(session: AsyncSession, delete_id: int):
    stmt = delete(Products).where(Products.id == delete_id)

    await session.execute(stmt)
    await session.commit()


async def add_new_product(session: AsyncSession, newProduct: Product):
    stmt = select(Products)

    result: Result = await session.execute(stmt)

    products = result.scalars().all()

    product = Products(**newProduct.model_dump(), id=len(products))

    session.add(product)
    await session.commit()
