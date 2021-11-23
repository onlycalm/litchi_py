##
# @file detvw.py
# @brief 检测可视化模块。
# @details 无
# @author Calm
# @date 2021-09-08
# @version v1.0.0
# @copyright Calm
#

from PySide2.QtWidgets import QTreeWidget, QTreeWidgetItem
from log import *

##
# @class cDetVw
# @brief 检测浏览控件。
# @details 基于tableWidget控件，浏览检测记录。
# @note 无
# @attention 无
#
class cDetVw:
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @param Obj 指向已有对象。
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self, Obj = None):
        LogTr("Enter cDetVw.__init__().")
        if Obj:
            self.Tw = Obj
        else:
            self.Tw = QTreeWidget()
        LogTr("Exit cDetVw.__init__().")

    ##
    # @brief 添加一条检测记录。
    # @details 往DetVw控件中添加一条检测记录。
    # @param self 对象指针。
    # @param Rec 一条Det记录，类型为列表。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ApdRec(self, Rec):
        LogTr("Enter cDetVw.ApdRec().")
        self.Tw.addTopLevelItem(QTreeWidgetItem(Rec)) #添加一项
        LogTr("Exit cDetVw.ApdRec().")

    ##
    # @brief 添加一条子检测记录。
    # @details 往DetVw控件中添加一条子检测记录。
    # @param self 对象指针。
    # @param Rec 一条Det记录，类型为列表。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ApdSubLvRec(self):
        pass

    ##
    # @brief 清空Det记录。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def Clr(self):
        LogTr("Enter cDetVw.Clr().")
        self.Tw.clear()
        LogTr("Exit cDetVw.Clr().")
