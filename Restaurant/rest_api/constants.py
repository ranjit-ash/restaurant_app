"""
Application Constant module
"""
# USER = "postgres"
# PASSWORD = "admin"
# HOST = "192.168.29.195"
# PORT = "5432"


USER = "postgres"
PASSWORD = "root"
HOST = "192.168.99.100"
PORT = "30432"

DATABASE = "restaurant_db"
DB_TABLE = "restaurant_tb"
TABLE_COLUMNS = ['business_id', 'business_name', 'business_address', 'business_city', 'business_state',
                 'business_postal_code', 'business_latitude', 'business_longitude', 'business_location',
                 'business_phone_number', 'inspection_id', 'inspection_date', 'inspection_score',
                 'inspection_type', 'violation_id', 'violation_description', 'risk_category', 'status']

SUCCESS_STATUS = 200
DB_ERROR_STATUS = 503
PARAMETER_ERROR = 400
PARAMETER_ERROR_MSG = {"error": "not valid key"}







