from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

logging.info("Hello Logging Check !")

try:
    b = 1 / 0
except Exception as e:
    exception = USvisaException(e,sys)
    logging.error(str(exception))
    raise exception

logging.info("hello world")
