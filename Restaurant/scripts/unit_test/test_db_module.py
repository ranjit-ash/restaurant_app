from models.db_module import POSTGRES_DB
from rest_api.constants import USER, PASSWORD, HOST, PORT, DATABASE
import unittest


class My_db_module(unittest.TestCase):
    def test_object(self):
        connection = POSTGRES_DB(user=USER,
                                 password=PASSWORD,
                                 host=HOST,
                                 database=DATABASE,
                                 port=PORT)
        self.assertIsInstance(connection, POSTGRES_DB)
        connection.close()


