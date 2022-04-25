from dataclasses import dataclass

import pymysql
from pymysql import Connection
from pymysql.cursors import Cursor, DictCursor


# #*********************************************************************************************************************
@dataclass
class Database(object):
    def __init__(self, host: str, user: str, password: str, db: str, charset: str = 'utf8', port: int = 3306):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.port = port

    def _get_connection(self) -> Connection:
        return pymysql.connect(host=self.host,
                               user=self.user,
                               password=self.password,
                               db=self.db,
                               charset=self.charset,
                               port=self.port)

    def execute_query(self, sql: str) -> int:
        with self._get_connection() as con:
            with con.cursor() as cur:
                result = cur.execute(sql)
                con.commit()
                return result

    def select_query(self, sql: str, result_type: Cursor = DictCursor):
        with self._get_connection() as con:
            with con.cursor(result_type) as cur:
                cur.execute(sql)
                return cur.fetchall()

    def select_one_query(self, sql: str, result_type: Cursor = DictCursor):
        with self._get_connection() as con:
            with con.cursor(result_type) as cur:
                cur.execute(sql)
                return cur.fetchone()

    def select_many_query(self, sql: str, size: int = 1, result_type: Cursor = DictCursor):
        with self._get_connection() as con:
            with con.cursor(result_type) as cur:
                cur.execute(sql)
                return cur.fetchmany(size)
