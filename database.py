import logging
import sqlite3
from sqlite3 import Error


class database:
    def __init__(self, name: str) -> None:
        self.__connection = self.__connect(name)
        if self.__connection != None:
            self.__cursor = self.__connection.cursor()
            self.__create()
        else:
            print('Retry')

    def __connect(self, name):
        conn = None
        try:
            conn = sqlite3.connect(name)
            logging.info(print(sqlite3.version))
        except Error as e:
            logging.info(print(e))
        return conn

    def __create(self):
        self.__cursor.execute(
            '''CREATE TABLE IF NOT EXISTS data (
                id INT PRIMARY KEY,
                url TEXT, 
                headline TEXT,
                author TEXT,
                date TEXT
                ) STRICT
                ''')

    def getkeyindex(self):
        query = '''SELECT MAX(id) as mid FROM data
        '''
        res = self.__cursor.execute(query).fetchone()[0]

        logging.debug('last index is %s', res)
        return res

    def insert(self, data):
        logging.info('Inserting data')
        query = '''INSERT into data VALUES(?,?,?,?,?)'''
        for r in data:
            try:
                self.__cursor.execute(query, (
                    r['id'], r['url'], r['headline'], r['author'], r['date']))
                self.__connection.commit()
            except sqlite3.Error as er:
                logging.info(er)
            finally:
                continue

    def fetchall(self):
        query = '''SELECT * FROM data'''
        res = self.__cursor.execute(query).fetchall()
        return res

    def deduplicate(self):
        query = '''SELECT  FROM data'''

    def close(self):
        self.__cursor.close()
        self.__connection.close()
