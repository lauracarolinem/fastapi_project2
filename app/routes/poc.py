#proof of concept
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.routes.deps import get_db_session
from app.schemas.category import CategoryOutput
from app.db.models import Category as CategoryModel
from fastapi_pagination import add_pagination, paginate, Page, LimitOffsetPage

router = APIRouter(prefix='/poc', tags=['POC'])

@router.get('/list', response_model=Page[CategoryOutput]) #gera todas as paginas igualmente
@router.get('/list/limit-offset', response_model=LimitOffsetPage[CategoryOutput]) #limit offset tem dois parametros na documentação. Limit=quantos, offset=a partir de qual
def list_categories():
    categories = [
        CategoryOutput(name=f'category {n}', slug=f'category-{n}', id=n)
        for n in range(100)
    ]
    
    return paginate(categories)

add_pagination(router)

