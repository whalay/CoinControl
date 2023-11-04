from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def check_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            if current_user.verified is False:
                flash('Please confirm your email address', 'danger')
                return redirect(url_for('auth.unconfirmed'))
        else:
            flash('Session has expired please login to access this page', 'danger')
            return redirect(url_for('auth.login'))
        
        return func(*args, **kwargs)
                              
    return decorated_function


