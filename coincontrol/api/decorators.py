from flask import request
import datetime
from functools import wraps

# decorator for returning the code execution time, monitoring cookies and IP addresses.
def monitor(function=None):
    @wraps(function)
    def wrapper(*args, **kwargs):
        s=datetime.datetime.now()
        _=function(*args, **kwargs)
        e=datetime.datetime.now()
        print("Execution Time:{}".format(e-s))
        print("Ip Address  : {} ".format(request.remote_user))
        print("Cookies : {} ".format(request.cookies))
        print(request.user_agent)
        return _
    return wrapper


