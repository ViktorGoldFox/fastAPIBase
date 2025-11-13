from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str

class Getting_product(BaseModel):
    name: str