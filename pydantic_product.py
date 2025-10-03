from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Цена должна быть больше 0")
    tags: list[str] = []


product_data = {
    "name": "Phone",
    "price": 499.99,
    "tags": ["electronics", "smartphone"]
}

product = Product(**product_data)
print(product)
