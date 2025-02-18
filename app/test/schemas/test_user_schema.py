from app.schemas.user import User #ainda nao foi criado na pasta schemas 
import pytest


def test_user_schema():
    user = User(username='Laura', password='pass#')
    
    assert user.model_dump() == {
        'username': 'Laura',
        'password': 'pass#'
    }
    
def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username='Laura#', password='pass#')
    
    

