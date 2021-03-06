import functools
import logging


def create_logger():
    """
    Creates a logging object and returns it
    """
    logging.basicConfig(filename="Log.log", level=logging.WARNING,
                        format='[%(funcName)s]:%(message)s')
    return logging


def logger_exception(function):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        log = create_logger()
        try:
            return function(*args, **kwargs)
        except Exception:
            log.exception("Error compiling data in: %s,\n %s"
                          , function.__name__, function.__doc__)
            # re-raise the exception
            raise

    return wrapper
