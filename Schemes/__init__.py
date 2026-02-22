from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str


class GettingProduct(BaseModel):
    name: str
