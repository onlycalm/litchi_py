import logging

logging.basicConfig(level = logging.DEBUG, format = '[%(levelname)s]-[%(filename)s <%(lineno)s>](%(funcName)s): %(message)s')

PrtLogCrt = logging.critical
PrtLogErr = logging.error
PrtLogWrn = logging.warning
PrtLogDbg = logging.debug
PrtLogInfo = logging.info
