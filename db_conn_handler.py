import config_reader
import db_postgres


class ConnectionHandler:

    @classmethod
    def set_db_connection(cls):
        if config_reader.database_type == "postgres":
            return db_postgres.PostgresConnection(config_reader.database_url)
        elif config_reader.database_type == "mysql":
            pass
        elif config_reader.database_type == "spreadsheets":
            pass
        else:
            return db_postgres.PostgresConnection(config_reader.database_url)

