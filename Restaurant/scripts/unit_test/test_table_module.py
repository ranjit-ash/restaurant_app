from rest_api.connection_util import connectdb, tabledb
from rest_api.constants import DB_TABLE
import unittest
from rest_api.api_ops import selectdb, selectByDatedb, updatedb, deletedb, insertdb


class My_db_table(unittest.TestCase):
    def test_object(self):
        conn = connectdb()
        tb = tabledb(conn, DB_TABLE)
        dummy_table = {
            "business_address": "dummy address",
            "business_city": "dummy city",
            "business_id": "00000",
        }
        result, status = insertdb(tb, dummy_table)
        self.assertEqual(type(result), dict)
        self.assertEqual(status, 200)
        query_parameters = {"business_id": "00000"}
        update_parameters = {"business_address": "dummy address update",
                             "business_city": "dummy city updated",
                             }
        result, status = updatedb(tb, query_parameters, update_parameters)
        self.assertEqual(type(result), dict)
        self.assertEqual(status, 200)
        query_parameters = {"business_id": "00000"}
        result, status = deletedb(tb, query_parameters)
        self.assertEqual(type(result), dict)
        self.assertEqual(status, 200)
