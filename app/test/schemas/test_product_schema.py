from app.schemas.product import Product 
import pytest

#validação
def test_product_schema():
    product = Product(
        name='Camisa Mike',
        slug='camisa-mike',
        price=22.99,
        stock=22
    ) #instanciando um produto 
    
    assert product.model_dump() == {
        'name': 'Camisa Mike',
        'slug': 'camisa-mike',
        'price': 22.99,
        'stock': 22    
    }
    
def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='camisa mike',
            price=22.99,
            stock=22
        )
        
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='camisão',
            price=22.99,
            stock=22
        )
        
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='Camisa-Mike',
            price=22.99,
            stock=22
        )

#o preço nao pode ser menor ou igual a 0
def test_product_schema_invalid_price():
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='camisa-mike',
            price=-8.50,
            stock=22
        )