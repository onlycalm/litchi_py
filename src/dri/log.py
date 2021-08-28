import logging

logging.basicConfig(level = logging.DEBUG, format = '[%(levelname)s]-[%(filename)s <%(lineno)s>](%(funcName)s): %(message)s')
LogStrEntFun = "<-----Enter function----->"
LogStrExFun = "<-----Exit function----->"

PrtLogCrt = logging.critical
PrtLogErr = logging.error
PrtLogWrn = logging.warning
PrtLogInfo = logging.info
PrtLogDbg = logging.debug
