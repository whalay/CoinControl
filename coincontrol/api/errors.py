# from coincontrol.extensions import jwt
# from coincontrol.api.blacklist import BLACKLIST
# from coincontrol.models import Users

# @jwt.user_identity_loader
# def user_identity_lookup(user):
#     return user.user_id

# @jwt.user_lookup_loader
# def user_lookup_callback(_jwt_header, jwt_data):
#     identity = jwt_data["sub"]
#     return Users.query.filter_by(user_id=identity).one_or_none()

# @jwt.token_in_blocklist_loader
# def check_if_token_in_blocklist(jwt_header, jwt_payload):
#     return jwt_payload["jti"] in BLACKLIST

# @jwt.revoked_token_loader
# def revoked_token_callback(jwt_header, jwt_payload):
#     response = {
#         "status": 401,
#         "message": "User has been logged out",
#         "data": {
#             "error": "token_revoked",
#         },
#     }
#     return response, 401

# @jwt.invalid_token_loader
# def invalid_token_callback(jwt_header, jwt_payload):
#     response = {
#         "status": 422,
#         "message": "Invalid token",
#         "data": {
#             "error": "This token is invalid",
#         },
#     }
#     return response, 422

# @jwt.expired_token_loader
# def expired_token_callback(jwt_header, jwt_payload):
#     response ={
#         "status": 400,
#         "message": "Expired token",
#         "data": {
#             "error": "This token has expired",
#         },
#     }
#     return response, 400