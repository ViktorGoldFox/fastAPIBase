from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str


class NewProduct(BaseModel):
    name: str
