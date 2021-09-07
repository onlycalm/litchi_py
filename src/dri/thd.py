##
# @file thd.py
# @brief 线程模块。
# @details 无
# @author Calm
# @date 2021-09-07
# @version v1.0.0
# @copyright Calm
#

from PySide2.QtCore import QThread

##
# @class cThd
# @brief 线程类。
# @details 无
# @note 无
# @attention 无
#
class cThd(QThread):
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @param Id 线程Id。
    # @param Nm 线程名。
    # @param Cb 线程回调。
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self, Id, Nm, Cb):
        QThread.__init__(self)
        self.Id = Id
        self.Nm = Nm
        self.Cb = Cb

    ##
    # @brief 线程执行入口函数。
    # @details 启动线程后将会首先调用该函数。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 该函数内部将调用线程回调函数。
    #
    def run(self):
        if self.Cb:
            self.Cb(self.Id, self.Nm)

    ##
    # @brief 绑定线程回调函数。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SetCb(self, Cb):
        self.Cb = Cb

    ##
    # @brief 启动线程。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def Strt(self):
        QThread.start(self)
