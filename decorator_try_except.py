import logging
import traceback
import flask
from functools import wraps

def try_except(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except:
            result = {
                "code": "some_code",
                "msg": "API fail"
            }
            logging.info(traceback.format_exc())
        finally:
            return flask.jsonify(result)
    return wrapper
