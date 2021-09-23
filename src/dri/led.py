##
# @file led.py
# @brief Led模块。
# @details 方便状态提示
# @author Calm
# @date 2021-09-23
# @version v1.0.0
# @copyright Calm
#

from PySide2.QtWidgets import QLabel
from log import *

##
# @class cLed
# @brief Led控件。
# @details 无
# @note 无
# @attention 无
#
class cLed:
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @param Obj 指向已有对象。
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self, Obj = None, Clr = None):
        LogTr("Enter cLogVw.__init__().")
        if Obj:
            self.Lbl = Obj
        else:
            self.Lbl = QLabel()

        self.Clr = Clr #Led颜色。
        self.SwSta = False #Led开关状态。
        LogTr("Exit cLogVw.__init__().")

    ##
    # @brief 设置Led颜色。
    # @details 无
    # @param self 对象指针。
    # @param Clr 颜色，为RGB值。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SetClr(self, Clr):
        LogTr("Enter cLogVw.SetClr().")
        self.Clr = Clr
        LogTr("Exit cLogVw.SetClr().")

    ##
    # @brief 设置Led字符串。
    # @details 无
    # @param self 对象指针。
    # @param Str 字符串。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SetStr(self, Str):
        LogTr("Enter cLogVw.SetStr().")
        self.Lbl.setText(Str)
        LogTr("Exit cLogVw.SetStr().")

    ##
    # @brief 开关Led。
    # @details 无
    # @param self 对象指针。
    # @param SwSta 开关状态，布尔型。
    # @arg True 点亮。
    # @arg False 熄灭。
    # @return 无
    # @note 无
    # @attention 无
    #
    def Sw(self, SwSta):
        LogTr("Enter cLogVw.Sw().")
        self.SwSta = SwSta
        if self.SwSta:
            self.Lbl.setStyleSheet(f"background-color:{self.Clr};")
        else:
            self.Lbl.setStyleSheet("background-color:none;")
        LogTr("Exit cLogVw.Sw().")

    ##
    # @brief 获取Led开关状态。
    # @details 无
    # @param self 对象指针。
    # @return Led状态，布尔型。
    # @note 无
    # @attention 无
    #
    def GetSwSta(self):
        return self.SwSta
