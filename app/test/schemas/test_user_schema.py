from app.schemas.user import User, TokenData #ainda nao foi criado na pasta schemas 
import pytest
from datetime import datetime


def test_user_schema():
    user = User(username='Laura', password='pass#')
    
    assert user.model_dump() == {
        'username': 'Laura',
        'password': 'pass#'
    }
    
def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username='Laura#', password='pass#')
    

def test_token_date():
    expires_at = datetime.now()
    token_data = TokenData(
        access_token = 'token qualquer',
        expires_at = expires_at
    )
    
    assert token_data.model_dump() == {
        'access_token': 'token qualquer',
        'expires_at': expires_at
    }
    
