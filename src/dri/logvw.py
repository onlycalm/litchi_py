##
# @file logvw.py
# @brief log view模块。
# @details 方便查看Log
# @author Calm
# @date 2021-09-08
# @version v1.0.0
# @copyright Calm
#

from PySide2.QtWidgets import QTreeWidget, QTreeWidgetItem

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
    # @param Obj TreeWidget对象。
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self, Obj = None):
        if Obj:
            self.Tw = Obj
        else:
            self.Tw = QTreeWidget()

    ##
    # @brief 添加Log记录。
    # @details 往LogVw控件中添加一条Log记录。
    # @param self 对象指针。
    # @param Rec 类型为列表，一条Log记录。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ApdLog(self, Rec):
        self.Tw.addTopLevelItem(QTreeWidgetItem(Rec)) #添加一项

    ##
    # @brief 清空Log记录。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClrLog(self):
        self.Tw.clear()
