from sqlalchemy import select, update, delete, Result
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import *
from untities import *


async def get_all_product(session: AsyncSession):
    stmt = (
        select(Products)
    )

    result: Result = await session.execute(stmt)

    objects = result.scalars().all()

    return objects


async def delete_product(session: AsyncSession, delete_id: int) -> bool:
    stmt = (
        delete(Products)
        .where(Products.id == delete_id)
    )

    await session.execute(stmt)
    await session.commit()

    return True


async def add_new_product(session: AsyncSession, new_product: Product) -> bool:
    stmt = (
        select(Products)
    )

    result: Result = await session.execute(stmt)

    products = result.scalars().all()

    product = Products(**new_product.model_dump(), id=len(products))

    session.add(product)
    await session.commit()

    return True