from app.db.models import Product as ProductModel #modelo
from app.db.models import Category as CategoryModel #modelo
from app.schemas.product import Product #validacao
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status

class ProductUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        
    def add_product(self, product: Product, category_slug: str):
        category = self.db_session.query(CategoryModel).filter_by(slug=category_slug).first()
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Category not found with slug {category_slug}')

        product_model = ProductModel(**product.model_dump())
        product_model.category_id = category.id
        
        self.db_session.add(product_model)
        self.db_session.commit()
    