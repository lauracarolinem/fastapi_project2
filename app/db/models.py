from app.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, func
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = 'categories'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
    products = relationship('Product', back_populates='category')
    
class Product(Base):
    __tablename__ = 'products'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
    price = Column('price', Float)
    stock = Column('stock', Integer)
    created_at = Column('created_at', DateTime, server_default=func.now()) #server update é pra toda vez que for criar
    updated_at = Column('updated_at', DateTime, onupdate=func.now()) #on update é pra toda vez que for atualizado
    category_id = Column('category_id', ForeignKey('categories.id'), nullable=False)
    
    #criar relaçoes entre produto e categoria
    #ou seja, poder saber qual a categoria do produto diretamente, por exemplo: product.categories.name
    category = relationship('Category', back_populates='products')
    
    