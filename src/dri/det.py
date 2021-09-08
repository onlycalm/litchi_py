##
# @file det.py
# @brief 检测模块。
# @details 无
# @author Calm
# @date 2021-09-08
# @version v1.0.0
# @copyright Calm
#

from PySide2.QtWidgets import QTableWidget

##
# @class cDetVw
# @brief 检测记录浏览器类。
# @details 基于tableWidget控件，浏览检测记录。
# @note 无
# @attention 无
#
class cDetVw:
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @param Bg
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self, Obj):
        if Obj:
            self.TblWg = Obj
        else:
            self.TblWg = QTableWidget()
