from os import environ
from time import sleep
from typing import List, Tuple, Type, Union

import mysql.connector
from mysql.connector.errors import InternalError, OperationalError

from src.base_logger import logger


class Database:

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        Context Manager for connecting to db in a with block.
        """
        self.connection = self.connect()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if self.cursor is not None:
            if exc_type is not None:
                self.rollback()
            else:
                self.commit()
            self.close()

    class Decorators:
        @staticmethod
        def retry(tries: int, delay: float, exceptions: Tuple[Type[Exception], ...]):
            """
            Retry Decorator
            Retries the wrapped function/method `times` times if the exceptions listed in ``exceptions`` are thrown
            """

            def decorator(func):
                def newfn(*args, **kwargs):
                    attempt = 0
                    while attempt < tries:
                        try:
                            return func(*args, **kwargs)
                        except exceptions as e:
                            logger.warning('Exception %s thrown when attempting to run %s, attempt %d of %d' %
                                           (e, func, attempt, tries)
                                           )
                            sleep(delay)
                            attempt += 1
                    return func(*args, **kwargs)

                return newfn

            return decorator

    @Decorators.retry(tries=3, delay=5, exceptions=(OperationalError, InternalError))
    def connect(self):
        connection = mysql.connector.connect(
            host=environ['DB_HOST'],
            port=int(environ['DB_PORT']),
            user=environ['DB_USER'],
            password=environ['DB_PASSWORD'],
            db=self.db_name,
            autocommit=False)
        return connection

    def select_one(self, sql, args: Union[list, tuple] = None) -> Tuple:
        self.execute(sql, args)
        return self.cursor.fetchone()

    def select_all(self, sql, args: Union[list, tuple] = None) -> List[Tuple]:
        self.execute(sql, args)
        return self.cursor.fetchall()

    def commit(self) -> None:
        logger.debug('Committing to DB...')
        assert self.cursor is not None
        self.connection.commit()

    def rollback(self) -> None:
        logger.warning('Rolling back changes to DB...')
        assert self.cursor is not None
        self.connection.rollback()

    def close(self) -> None:
        logger.debug('DB closing connection')
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def execute(self, sql, args: Union[list, tuple] = None) -> None:
        self.cursor.execute(sql, args)
