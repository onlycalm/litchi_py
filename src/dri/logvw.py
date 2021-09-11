##
# @file logvw.py
# @brief log可视化模块。
# @details 方便查看Log
# @author Calm
# @date 2021-09-08
# @version v1.0.0
# @copyright Calm
#

from PySide2.QtWidgets import QTableWidget
from PySide2.QtWidgets import QTableWidgetItem
from log import *

##
# @class cLogVw
# @brief Log浏览控件。
# @details 无
# @note 无
# @attention 无
#
class cLogVw:
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
        LogTr("Enter cLogVw.__init__().")
        if Obj:
            self.Tw = Obj
        else:
            self.Tw = QTableWidget()
        LogTr("Exit cLogVw.__init__().")

    ##
    # @brief 设置一个表格单元内容。
    # @details 无
    # @param self 对象指针。
    # Wparam Row 行号。
    # Wparam Col 列号。
    # @param Rec 类型为字符串，内容。
    # @return 无
    # @note 无
    # @attention 索引从0行0列开始
    #
    def SetCell(self, Row, Col, Rec):
        LogTr("Enter cLogVw.SetCell().")
        self.Tw.setItem(Row, Col, QTableWidgetItem(Rec))
        LogTr("Exit cLogVw.SetCell().")

    ##
    # @brief 清空Log记录。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClrLog(self):
        LogTr("Enter cLogVw.ClrLog().")
        self.Tw.clear()
        LogTr("Exit cLogVw.ClrLog().")

    ##
    # @brief 设置行数量。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SetRowAmt(self, RowAmt):
        LogTr("Enter cLogVw.SetRowAmt().")
        self.Tw.setRowCount(RowAmt)
        LogTr("Exit cLogVw.SetRowAmt().")

    ##
    # @brief 设置列数量。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SetColAmt(self, ColAmt):
        LogTr("Enter cLogVw.SetColAmt().")
        self.Tw.setColumnCount(ColAmt)
        LogTr("Exit cLogVw.SetColAmt().")

    ##
    # @brief 设置表格单元格背景色。
    # @details 无
    # @param self 对象指针。
    # Wparam Row 行号。
    # Wparam Col 列号。
    # @param Clr 颜色。
    # @return 无
    # @note 无
    # @attention 索引从0行0列开始。
    # @example 用法示例。
    # @code
    #   self.Tw.SetCellBgClr(0, 1, QColor(Qt.red))
    # @encode
    #
    def SetCellBgClr(self, Row, Col, Clr):
        LogTr("Enter cLogVw.SetCellBgClr().")
        self.Tw.item(Row, Col).setBackground(Clr)
        LogTr("Exit cLogVw.SetCellBgClr().")
