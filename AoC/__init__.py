import logging as _logging
import sys as _sys


import dotenv as _dotenv
_dotenv.load_dotenv()
    
_stdoutHandler = _logging.StreamHandler(_sys.stdout)
_stdoutHandler.addFilter(lambda record: record.levelno < _logging.WARNING)
_stderrHandler = _logging.StreamHandler(_sys.stderr)
_stderrHandler.addFilter(lambda record: record.levelno >= _logging.WARNING)

_logging.basicConfig(
    format = "[%(asctime)s:%(msecs)03d]-[%(levelname)s]: %(message)s",
    datefmt = "%H:%M:%S",
    level = _logging.INFO,
    handlers = [_stdoutHandler, _stderrHandler]
)


from .Challenge import *

from .getInput import *