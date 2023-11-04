from flask_restful import Api as _Api
from werkzeug.exceptions import HTTPException


class Api(_Api):
    def error_router(self, original_handler, e):
        """
        Flask restful in gobbles up all errors once debug is turned off.
        This is not a desired outcome, as validation errors from marshmallow
        ends up getting caught up in this and returns as an internal server errror.
        So we override the error_router here and allow flask handle all non HTTP errors instead
        based on the defined error handlers.
        """
        if self._has_fr_route() and isinstance(e, HTTPException):
            try:
                # Use Flask-RESTful's error handling method
                return self.handle_error(e)
            except Exception:
                # Fall through to original handler (i.e. Flask)
                pass
        return original_handler(e)