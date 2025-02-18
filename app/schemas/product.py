from app.schemas.base import CustomBaseModel
from app.schemas.category import Category
from pydantic import field_validator
import re

class Product(CustomBaseModel):
    name: str
    slug: str
    price: float
    stock: int
    
    
    @field_validator('slug')
    def validate_slug(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('Invalid slug')
        return value 
    
    @field_validator('price')
    def validate_price(cls, value):
        if value <= 0:
            raise ValueError('Price can\'t be lower or equal to 0')
        return value 
    
class ProductInput(CustomBaseModel):
    category_slug: str
    product: Product
    

class ProductOutput(Product):
    id: int
    category: Category