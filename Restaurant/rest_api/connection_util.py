"""
Connection functions
"""
from models.db_module import *
from models.table_module import *
from rest_api.constants import USER, PASSWORD, HOST, PORT, DATABASE


def connectdb():
    connection = POSTGRES_DB(user=USER,
                             password=PASSWORD,
                             host=HOST,
                             database=DATABASE,
                             port=PORT,)

    return connection


def tabledb(conn, table):
    return TABLE(conn, table)
