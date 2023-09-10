import pytest

from src.database import Database


@pytest.fixture(scope="session")
def mock_db():
    with Database('mock_db') as db:
        yield db
