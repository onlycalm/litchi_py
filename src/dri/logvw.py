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
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor
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

        self.LvClr = {"CRITICAL":QColor("#FF00FF"), "ERROR":QColor(Qt.red), "WARNING":QColor(Qt.yellow),
                      "SUCCESS":QColor(Qt.green)}
        LogTr("Exit cLogVw.__init__().")

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
    # @brief 获取表格行数。
    # @details 无
    # @param self 对象指针。
    # @return 行数
    # @note 无
    # @attention 无
    #
    def GetRowAmt(self):
        LogTr("Enter cLogVw.GetRowAmt().")
        LogTr("Exit cLogVw.GetRowAmt().")
        return self.Tw.rowCount()

    ##
    # @brief 获取表格列数。
    # @details 无
    # @param self 对象指针。
    # @return 列数
    # @note 无
    # @attention 无
    #
    def GetColAmt(self):
        LogTr("Enter cLogVw.GetColAmt().")
        LogTr("Exit cLogVw.GetColAmt().")
        return self.Tw.columnCount()

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
    #   self.SetCellBgClr(0, 1, QColor(Qt.red))
    # @encode
    #
    def SetCellBgClr(self, Row, Col, Clr):
        LogTr("Enter cLogVw.SetCellBgClr().")
        self.Tw.item(Row, Col).setBackground(Clr)
        LogTr("Exit cLogVw.SetCellBgClr().")

    ##
    # @brief 选中单元格的背景颜色。
    # @details 无
    # @param self 对象指针。
    # @param Clr 颜色，类型为字符串。
    # @return 无
    # @note 无
    # @attention 索引从0行0列开始。
    # @example 用法示例。
    # @code
    #   self.SetSelBgClr("grey")
    # @encode
    #
    def SetSelBgClr(self, Clr):
        LogTr("Enter cLogVw.SetSelBgClr().")
        self.Tw.setStyleSheet(f"selection-background-color:{Clr};")
        LogTr("Exit cLogVw.SetSelBgClr().")

    ##
    # @brief 设置一个表格单元内容。
    # @details 无
    # @param self 对象指针。
    # @param Row 行号。
    # @param Col 列号。
    # @param Rec 内容，类型为字符串，。
    # @return 无
    # @note 无
    # @attention 索引从0行0列开始。
    #
    def SetCell(self, Row, Col, Rec):
        LogTr("Enter cLogVw.SetCell().")
        self.Tw.setItem(Row, Col, QTableWidgetItem(Rec))
        LogTr("Exit cLogVw.SetCell().")


    ##
    # @brief 获取一个表格单元内容。
    # @details 无
    # @param self 对象指针。
    # @param Row 行号。
    # @param Col 列号。
    # @return 内容，类型为字符串。
    # @note 无
    # @attention 索引从0行0列开始。
    #
    def GetCell(self, Row, Col):
        LogTr("Enter cLogVw.SetCell().")
        return self.Tw.item(Row, Col).text()
        LogTr("Exit cLogVw.SetCell().")

    ##
    # @brief 添加一条Log记录。
    # @details 往LogVw控件中添加一条Log记录。
    # @param self 对象指针。
    # @param Rec 一条Log记录，类型为列表。
    # @return 无
    # @note 无
    # @attention 索引从0行0列开始。
    #
    def ApdRec(self, Rec):
        LogTr("Enter cDetVw.ApdRec().")
        RowAmt = self.GetRowAmt()
        self.SetRowAmt(RowAmt + 1)
        RecAmt = len(Rec)

        if RecAmt <= self.GetColAmt():
            for i in range(RecAmt):
                self.SetCell(RowAmt, i, Rec[i])
        LogTr("Exit cDetVw.ApdRec().")

    ##
    # @brief 清空Log记录。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def Clr(self):
        LogTr("Enter cLogVw.Clr().")
        self.Tw.clear()
        LogTr("Exit cLogVw.Clr().")

    ##
    # @brief 高亮Log等级。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 高亮颜色由
    #
    def HlLogLv(self, Row, Col, Lv):
        LogTr("Enter cLogVw.HlLogLv().")
        if Lv in self.LvClr:
            self.SetCellBgClr(Row, Col, self.LvClr[Lv])
        LogTr("Exit cLogVw.HlLogLv().")
