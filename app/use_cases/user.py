from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from app.schemas.user import User, TokenData
from app.db.models import User as UserModel
from fastapi.exceptions import HTTPException
from fastapi import status
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from decouple import config

crypt_context = CryptContext(schemes=['sha256_crypt'])
#openssl rand -hex 32
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')


class UserUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def register_user(self, user: User):
        user_on_db = UserModel(
            username = user.username,
            password=crypt_context.hash(user.password)
        )
        
        self.db_session.add(user_on_db)
        
        try:
            self.db_session.commit()
        except IntegrityError:
            self.db_session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username already exist')
    
    def user_login(self, user: User, expires_in: int = 30):
        user_on_db = self._get_user(username=user.username)
        
        if user_on_db is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid username or password')
        
        if not crypt_context.verify(user.password, user_on_db.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid username or password')
        
        expires_at = datetime.now(timezone.utc) + timedelta(expires_in)
        
        data = {
            'sub': user_on_db.username,
            'exp': expires_at
        }
        
        access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        token_data = TokenData(access_token=access_token, expires_at=expires_at)
        
        return token_data
    
    def verify_token(self, token: str):
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Expired token')
        
        user_on_db = self._get_user(username=data['sub'])
        if user_on_db is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid username')
    
    def _get_user(self, username: str):
        user_on_db = self.db_session.query(UserModel).filter_by(username=username).first()
        return user_on_db
        