import jwt
from flask import current_app


def decode_jwt(token):
    try:
        secret = current_app.config["SECRET_KEY"]
        payload = jwt.decode(token, str(secret), algorithms=["HS256"])
        return True, payload
    except jwt.ExpiredSignatureError:
        return False, "Token expired"
    except jwt.InvalidTokenError:
        return False, "Invalid token"
    except Exception as e:
        return False, str(e)
    
    
