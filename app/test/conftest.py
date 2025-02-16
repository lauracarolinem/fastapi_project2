from app.db.connection import Session
import pytest

@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()