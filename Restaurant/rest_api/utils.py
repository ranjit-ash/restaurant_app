"""
Common functions
"""
from datetime import datetime


def validateInputDict(input_dict, cmd_keys):
    for inputKey in input_dict:
        if inputKey not in cmd_keys:
            print(f"{inputKey}: input key is not defined in list of valid input parameters")
            return 1
    return 0


def getTimeStamp():
    current_time = datetime.now()
    current_time = str(current_time.strftime("%Y%m%d %H%M%S"))
    return current_time
