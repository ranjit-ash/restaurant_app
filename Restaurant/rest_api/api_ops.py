"""
Table operation specific to table
"""

from rest_api.utils import getTimeStamp


def selectdb(table):
    status, result = table.select(select_list=['*'], where_dict={})
    return result, status


def selectByDatedb(table, date):
    status, result = table.selectbydate(select_list=['*'], where_dict={'inspection_date': date})
    return result, status


def updatedb(table, query_parameters, update_parameters):
    if len(update_parameters) > 0:
        update_parameters.update({'inspection_date': getTimeStamp(),
                                  'status': 'new'})
    status, result = table.update(query_parameters, update_parameters)
    return result, status


def deletedb(table, query_parameters):
    status, result = table.delete(query_parameters)
    return result, status


def insertdb(table, query_parameters):
    status, result = table.insert(query_parameters)
    return result, status
