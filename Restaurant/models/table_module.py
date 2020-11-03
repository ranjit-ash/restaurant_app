from rest_api.constants import TABLE_COLUMNS, SUCCESS_STATUS, DB_ERROR_STATUS, PARAMETER_ERROR, PARAMETER_ERROR_MSG
from rest_api.utils import validateInputDict


class TABLE:
    """
        class to carry out database table operations
    """
    def __init__(self, connection, table):
        self.connection = connection
        self.table = table

    def create_table(self, column_dict):

        cmd = f"CREATE TABLE {self.table} ("
        for k, v in column_dict.items():
            cmd += f" {k} {v},"
        cmd = cmd.rstrip(",")
        cmd += f")"
        cursor = self.connection.get_cursor()
        cursor.execute(cmd)
        status_msg = cursor.statusmessage
        return SUCCESS_STATUS, {'result': status_msg}

    def insert(self, insert_dict):
        try:
            k_str = ""
            v_str = ""
            if validateInputDict(insert_dict.keys(), TABLE_COLUMNS):
                return PARAMETER_ERROR, PARAMETER_ERROR_MSG
            for k, v in insert_dict.items():
                if v is not None:
                    k_str += f"{k}, "
                    v_str += f"'{v}', "
            k_str = k_str.rstrip(", ")
            v_str = v_str.rstrip(", ")
            cmd = f"INSERT INTO {self.table} ({k_str}) VALUES ({v_str})"
            print(cmd)
            cursor = self.connection.get_cursor()
            cursor.execute(cmd)
            status_msg = cursor.statusmessage
            return SUCCESS_STATUS, {'result': status_msg}
        except Exception as e:
            print(f"error {e}")
            return DB_ERROR_STATUS, {'db_error': str(e)}

    def update(self, where_dict, update_dict):
        try:
            cmd = f"UPDATE {self.table} SET"
            set_val = ""
            for k, v in update_dict.items():
                set_val += f" {k} = '{v}',"
            set_val = set_val.rstrip(",")
            cmd += set_val

            where_val = "WHERE "
            for k, v in where_dict.items():
                where_val += f" {k} = '{v}' "
                # where_val = where_val.rstrip(",")
                cmd += where_val
            print(f"update cmd: {cmd}")
            cursor = self.connection.get_cursor()
            cursor.execute(cmd)
            status_msg = cursor.statusmessage
            return SUCCESS_STATUS, {'result': status_msg}
        except Exception as e:
            print(f"error {e}")
            return DB_ERROR_STATUS, {'db_error': str(e)}

    def delete(self, where_dict):
        try:
            if validateInputDict(where_dict.keys(), TABLE_COLUMNS):
                return PARAMETER_ERROR, PARAMETER_ERROR_MSG
            cmd = f"DELETE FROM {self.table}"
            where_val = " WHERE"
            for k, v in where_dict.items():
                where_val += f" {k} = '{v}',"
            where_val = where_val.rstrip(",")
            cmd += where_val
            cursor = self.connection.get_cursor()
            cursor.execute(cmd)
            status_msg = cursor.statusmessage
            return SUCCESS_STATUS, {'result': status_msg}
        except Exception as e:
            print(f"error {e}")
            return DB_ERROR_STATUS, {'db_error': str(e)}

    def select(self, select_list=['*'], where_dict={}):
        try:
            if validateInputDict(where_dict.keys(), TABLE_COLUMNS):
                return PARAMETER_ERROR, PARAMETER_ERROR_MSG
            select_string = ", ".join(select_list)
            cmd = f"SELECT {select_string} FROM {self.table}"
            where_val = " WHERE"
            for k, v in where_dict.items():
                where_val += f" {k} = '{v}',"
                where_val = where_val.rstrip(",")
                cmd += where_val
            cursor = self.connection.get_cursor()
            cursor.execute(cmd)
            columns = [desc[0] for desc in cursor.description]
            results = []
            for r in cursor:
                results.append(dict(zip(columns, r)))
            return SUCCESS_STATUS, {'result': results}

        except Exception as e:
            print(f"error {e}")
            return DB_ERROR_STATUS, {'db_error': str(e)}

    def selectbydate(self, select_list=['*'], where_dict={}):
        try:
            select_string = ", ".join(select_list)
            cmd = f"SELECT {select_string} FROM {self.table}"
            where_val = " WHERE"
            for k, v in where_dict.items():
                where_val += f" {k} <= '{v}',"
                where_val = where_val.rstrip(",")
                cmd += where_val
            print(f"----->command {cmd}")
            cursor = self.connection.get_cursor()
            cursor.execute(cmd)
            columns = [desc[0] for desc in cursor.description]
            results = []
            for r in cursor:
                results.append(dict(zip(columns, r)))
            return SUCCESS_STATUS, {'result': results}
        except Exception as e:
            print(f"error {e}")
            return DB_ERROR_STATUS, {'db_error': str(e)}
