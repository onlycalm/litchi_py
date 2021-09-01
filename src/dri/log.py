##
# @file log.py
# @brief log模块。
# @details 无
# @author Calm
# @date 2021-09-01
# @version v1.0.0
# @copyright Calm
#

import logging

logging.basicConfig(level = logging.DEBUG, format = '[%(levelname)s]-[%(filename)s <%(lineno)s>](%(funcName)s): %(message)s')
LogStrEntFun = "<-----Enter function----->"
LogStrExFun = "<-----Exit function----->"

PrtLogCrt = logging.critical
PrtLogErr = logging.error
PrtLogWrn = logging.warning
PrtLogInfo = logging.info
PrtLogDbg = logging.debug
