from flask import jsonify

class InvalidUsage(Exception):
    status_code = 400

    def init(self, message, status_code=None, payload=None):
        Exception.init(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv