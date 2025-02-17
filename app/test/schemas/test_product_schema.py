from app.schemas.product import Product, ProductInput
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

# o preço nao pode ser menor ou igual a 0
def test_product_schema_invalid_price():
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='camisa-mike',
            price=-8.50,
            stock=22
        )
        
# precisamos de um novo schema para criar a rota de add products pois o 
# json do test_product_routes->test_add_product_route_invalid_category é diferente do schema já feito nesse arquivo
def test_product_input_schema():
    product = Product(
        name='Camisa Mike',
        slug='camisa-mike',
        price=22.99,
        stock=22
    )
    
    product_input = ProductInput(
        category_slug='roupa',
        product= product
    )
    
    assert product_input.model_dump() == {
        "category_slug": "roupa",
        "product": {
            "name": "Camisa Mike",
            "slug": "camisa-mike",
            "price": 22.99,
            "stock": 22
        }
    }