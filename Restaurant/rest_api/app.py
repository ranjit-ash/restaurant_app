"""
Application factory module.
"""
from flask import request, Flask
from rest_api.api_ops import selectdb, selectByDatedb, updatedb, deletedb, insertdb
from rest_api.connection_util import connectdb, tabledb
import socket

app = Flask(__name__)


@app.route('/')
def index():
    """
    API function: to display welcome screen
    :return: <string>
    """
    return "Welcome to restaurant API"


@app.route('/<table>/select', methods=['GET'])
def select(table):
    """
    API function: to get table rows
    :param table: <string> DB table name
    :return: <dict> output of select query
    """
    conn = connectdb()
    tb = tabledb(conn, table)
    query_parameters = request.args
    result = selectdb(tb, query_parameters)
    conn.close()
    return result


@app.route('/<table>/select/<date>', methods=['GET'])
def selectByDate(table, date):
    """
    API function: to get table rows before modified date (YYYY-MM-DD)
    :param table: <string> DB table name
    :param table: <string> inspection date
    :return: <dict> output of select query
    """
    conn = connectdb()
    tb = tabledb(conn, table)
    result = selectByDatedb(tb, date)
    conn.close()
    return result


@app.route('/<table>/update', methods=['PUT'])
def update(table):
    """
    API function: update table rows based on payload
    :param table: <string> DB table name
    :return: <dict> output of update query
    """
    conn = connectdb()
    tb = tabledb(conn, table)
    query_parameters = request.args
    update_parameters = request.get_json()
    result = updatedb(tb, query_parameters, update_parameters)
    conn.close()
    return result


@app.route('/<table>/delete', methods=['DELETE'])
def delete(table):
    """
    API function: delete table rows url arguments
    :param table: <string> DB table name
    :return: <dict> output of delete query
    """
    conn = connectdb()
    tb = tabledb(conn, table)
    delete_parameters = request.args
    result, status = deletedb(tb, delete_parameters)
    conn.close()
    return result, status


@app.route('/<table>/insert', methods=['POST'])
def insert(table):
    """
    API function: insert row in table
    :param table: <string> DB table name
    :return: <dict> output of insert query
    """
    conn = connectdb()
    tb = tabledb(conn, table)
    insert_parameters = request.get_json()
    result = insertdb(tb, insert_parameters)
    conn.close()
    return result


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, )
