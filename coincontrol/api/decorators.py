from flask import request
import datetime
from functools import wraps
from flask_login import current_user

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

#decorator that only allow the admin user to assess the routes
def admin_required(function=None):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if current_user.is_admin != True:
            return {"message": "Admin access only"}, 403
        return function(*args, **kwargs)
    return wrapper

