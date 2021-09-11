##
# @file litchi.py
# @brief litchi主模块。
# @details 无
# @author Calm
# @date 2021-08-30
# @version v1.0.0
# @copyright Calm
#

import win
from log import *

##
# @class cLitchi
# @brief litchi主类。
# @details 该类用于构建litchi对象。
# @note 无
# @attention 无
#
class cLitchi:
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self):
        self.MainWin = win.cMainWin()

    ##
    # @brief 窗口显示函数。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def show(self):
        self.MainWin.show()
