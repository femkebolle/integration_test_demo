from os import environ
import pytest

from src.base_logger import logger
from src.database import Database
from src.sql.create_tables import TABLE_CREATION_QUERIES


def create_tables(db):
    assert db.db_name == 'mock_db'
    for query in TABLE_CREATION_QUERIES.values():
        db.execute(query)
    logger.info(f'Created {len(TABLE_CREATION_QUERIES)} table(s) for integration testing.')


def drop_tables(db):
    assert db.db_name == 'mock_db'
    for table_name in TABLE_CREATION_QUERIES.keys():
        db.execute(f'DROP TABLE {table_name};')
    logger.debug(f'Tests complete! Cleaned up by dropping {len(TABLE_CREATION_QUERIES)} table(s).')


@pytest.fixture(scope='session')
def mock_db():
    with Database(environ['DB_NAME']) as db:
        # setup tables
        create_tables(db)
        # yield the db as a fixture
        yield db
        # tear down tables now that the tests are done
        drop_tables(db)
