import pytest

from src.database import Database
from src.sql.create_tables import CREATE_SAMPLE_TABLE, TABLE_NAMES


def create_tables(db):
    assert db.db_name == 'mock_db'
    for query in [CREATE_SAMPLE_TABLE]:
        db.execute(query)


def drop_tables(db):
    assert db.db_name == 'mock_db'
    for table in TABLE_NAMES:
        db.execute(f'DROP TABLE {table};')


@pytest.fixture(scope="session")
def mock_db():
    with Database('mock_db') as db:
        # setup tables
        create_tables(db)
        # yield the db as a fixture
        yield db
        # tear down tables now that the tests are done
        drop_tables(db)
