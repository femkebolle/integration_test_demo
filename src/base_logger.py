import sys
from logging import StreamHandler, getLogger

from pythonjsonlogger import jsonlogger

stream_handler = StreamHandler()
formatter = jsonlogger.JsonFormatter(
    '%(asctime)s - %(module)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
)
stream_handler.setFormatter(formatter)
logger = getLogger()

logger.propagate = False

logger.addHandler(stream_handler)
# Specifying src stops external modules log messages, especially when on debug
logger = getLogger("src")
logger.setLevel('DEBUG')


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.error('Uncaught exception', exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception
