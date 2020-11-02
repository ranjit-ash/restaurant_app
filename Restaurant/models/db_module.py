import psycopg2
from psycopg2 import Error


class POSTGRES_DB:
    """
        class to carry out postgres database operations
    """
    def __init__(self, user, password, host, database, port='5432'):
        self.connection = psycopg2.connect(user=user,
                                           password=password,
                                           host=host,
                                           port=port,
                                           database=database)
        self.cursor = self.connection.cursor()

    def get_cursor(self):
        return self.cursor

    def get_connection(self):
        return self.connection

    def execute(self, *args, **kwargs):
        self.cursor.execute(*args, **kwargs)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.commit()
        self.cursor.close()
        self.connection.close()
        print("closed db connection")

    def set_isolation_level(self, level):
        self.connection.set_isolation_level(level);
        self.commit()


