from app.schemas.base import CustomBaseModel
from pydantic import field_validator
import re

class Category(CustomBaseModel):
    name: str
    slug: str
    
    @field_validator('slug')
    def validate_slug(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('Invalid slug')
        return value
    
    
class CategoryOutput(Category):
    id: int