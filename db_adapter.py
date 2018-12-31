import db_conn_handler


class DatabaseAdapter:
    database = db_conn_handler.ConnectionHandler.set_db_connection()

    @classmethod
    def get_version(cls):
        return cls.database.get_version()

    @classmethod
    def select_query(cls, query):
        return cls.database.select_query(query)

    @classmethod
    def insert_query(cls, query):
        return cls.database.insert_query(query)
