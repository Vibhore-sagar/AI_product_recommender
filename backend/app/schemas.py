from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: int
    name: str
    price: int
    category: str
    features: str

class RecommendationRequest(BaseModel):
    preference: str
    products: List[Product]
