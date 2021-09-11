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

logging.basicConfig(level = logging.NOTSET, format = '%(asctime)s [%(levelname)s]-(%(filename)s %(funcName)s %(lineno)s): %(message)s')
#logging.TRACE = 15
#logging.addLevelName(logging.TRACE, "TRACE")
#logging.log(logging.TRACE, "Test")

LogCrt = logging.critical #严重，Lv50。
LogErr = logging.error    #错误，Lv40。
LogWrn = logging.warning  #警告，Lv30。
LogInfo = logging.info    #信息，Lv20。
LogDbg = logging.debug    #调试，Lv10。
