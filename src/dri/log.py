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

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s [%(levelname)s]-(%(filename)s %(funcName)s %(lineno)s): %(message)s')
LogStrEntFun = "<-----Enter function----->"
LogStrExFun = "<-----Exit function----->"

LogCrt = logging.critical #严重。
LogErr = logging.error    #错误。
LogWrn = logging.warning  #警告。
LogInfo = logging.info    #信息。
LogDbg = logging.debug    #调试。
