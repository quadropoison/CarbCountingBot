from urllib import parse as urlparse
import psycopg2 as psycopg2


class PostgresConnection:

    def __init__(self, database_url):
        self._database_url = database_url
        self._parse_database_url()
        self.connection = None

    def _parse_database_url(self):
        self.parsed_url = urlparse.urlparse(self._database_url)

    def connect(self):
        return psycopg2.connect(
                    dbname=self.parsed_url.path[1:],
                    user=self.parsed_url.username,
                    password=self.parsed_url.password,
                    host=self.parsed_url.hostname,
                    port=self.parsed_url.port)

    def set_connection(self):
        if self.connection is None:
            self.connection = self.connect()
            return self.connection
        else:
            return self.connection

    def get_version(self):
        connection = self.set_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        return cursor.fetchall()

    def select_query(self, query):
        connection = self.set_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def insert_query(self, query):
        connection = self.set_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        return connection.commit()
