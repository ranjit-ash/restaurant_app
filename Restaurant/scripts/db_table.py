from models.db_module import *
from models.table_module import *
from rest_api.constants import USER, PASSWORD, HOST, PORT, DATABASE, DB_TABLE
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import requests


URL = "https://data.sfgov.org/resource/pyih-qa8i.json"
from collections import OrderedDict

table_column_datatype = OrderedDict()
table_column_datatype.update({"business_id": "text",
                              "business_name": "text",
                              "business_address": "text",
                              "business_city": "text",
                              "business_state": "text",
                              "business_postal_code": "text",
                              "business_latitude": "integer",
                              "business_longitude": "integer",
                              "business_location": "integer",
                              "business_phone_number": "text",
                              "inspection_id": "text",
                              "inspection_date": "timestamp",
                              "inspection_score": "integer",
                              "inspection_type": "text",
                              "violation_id": "text",
                              "violation_description": "text",
                              "risk_category": "text",
                              "status": "text"
                              })
try:
    connection = POSTGRES_DB(user=USER,
                             password=PASSWORD,
                             host=HOST,
                             database='postgres',
                             port=PORT, )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
    cursor = connection.get_cursor()
    db_create_cmd = f"create database {DATABASE};"
    cursor.execute(db_create_cmd)
    connection.close()
    connection = POSTGRES_DB(user=USER,
                             password=PASSWORD,
                             host=HOST,
                             database=DATABASE,
                             port=PORT, )
    table = TABLE(connection, DB_TABLE)
    table.create_table(table_column_datatype)
    r = requests.get(url=URL)
    sample_data = r.json()
    for i in range(10):
        table.insert(sample_data[i])
    connection.close()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    try:
        connection.close()
    except (Exception, psycopg2.Error) as error:
        print("Error closing postgres connection ", error)
    print("PostgreSQL connection is closed")

