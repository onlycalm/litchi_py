##
# @file pyqtgraph.py
# @brief 示波器模块。
# @details 无
# @author Calm
# @date 2021-08-30
# @version v1.0.0
# @copyright Calm
#

import pyqtgraph
from log import *

##
# @class cOsc
# @brief 示波器类。
# @details 该类用于构建基于pyqtgraph构建的波形显示功能。
# @note 无
# @attention 无
#
class cOsc:
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @param Bg
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self, Bg = "w", Fg = "k"):
        LogTr("Enter cOsc.__init__().")
        self.Ln = {}
        pyqtgraph.setConfigOption("background", Bg)
        pyqtgraph.setConfigOption("foreground", Fg)
        self.Pw = pyqtgraph.PlotWidget(enableAutoRange = True)
        LogTr("Exit cOsc.__init__().")

    ##
    # @brief 新增Line对象。
    # @details 无
    # @param self 对象指针。
    # @param Id Line ID编号，类型为任意字符串。
    # @param LnClr Line颜色。默认值为"k"即黑色。
    # @param LnWd Line宽度。默认值为1。
    # @param PtClr 点颜色。默认值为None。
    # @param PtSty 点样式。默认值为None。
    # @return 无
    # @note 无
    # @attention 无
    #
    def AddLn(self, Id, LnClr = "k", LnWd = 1, PtClr = None, PtSty = None):
        LogTr("Enter cOsc.AddLn().")
        self.Ln[Id] = {}
        self.Ln[Id]["LnClr"] = LnClr
        self.Ln[Id]["LnWd"] = LnWd
        self.Ln[Id]["PtClr"] = PtClr
        self.Ln[Id]["Sw"] = True
        self.Ln[Id]["Dat"] = []
        self.Ln[Id]["Plt"] = self.Pw.plot(pen = pyqtgraph.mkPen(color = LnClr, width = LnWd),
                                          symbolBrush = PtClr, symbol = PtSty)
        self.Ln[Id]["PtSty"] = PtSty
        LogTr("Exit cOsc.AddLn().")

    ##
    # @brief 删除Line对象。
    # @details 无
    # @param self 对象指针。
    # @param Id Line ID编号。
    # @return 无
    # @note 无
    # @attention 无
    #
    def DelLn(self, Id):
        LogTr("Enter cOsc.DelLn().")
        self.Ln[Id]["Plt"].setData([])
        del self.Ln[Id]
        LogTr("Exit cOsc.DelLn().")

    ##
    # @brief 删除Line对象。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClrAllLn(self):
        LogTr("Enter cOsc.ClrAllLn().")
        self.Ln.clear()
        self.Pw.clear()
        LogTr("Exit cOsc.ClrAllLn().")

    ##
    # @brief 设置Line数据。
    # @details 会覆盖原有数据。
    # @param self 对象指针。
    # @param Id Line ID编号。
    # @param Dat Line上点的数据，类型为整形列表。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SetDat(self, Id, Dat):
        LogTr("Enter cOsc.SetDat().")
        self.Ln[Id]["Dat"] = Dat
        self.Ln[Id]["Plt"].setData(Dat)
        LogTr("Exit cOsc.SetDat().")

    ##
    # @brief Line新增一个点数据。
    # @details Line末尾插入点。
    # @param self 对象指针。
    # @param Id Line ID编号。
    # @param Val 点的值。
    # @return 无
    # @note 无
    # @attention 一个点。
    #
    def ApdPt(self, Id, Val):
        LogTr("Enter cOsc.ApdPt().")
        self.Ln[Id]["Dat"].append(Val)
        self.Ln[Id]["Plt"].setData(self.Ln[Id]["Dat"])
        LogTr("Exit cOsc.ApdPt().")

    ##
    # @brief 设置Line属性。
    # @details 无
    # @param self 对象指针。
    # @param Id Line ID编号。
    # @param LnClr Line颜色。默认值为"k"即黑色。
    # @param LnWd Line宽度。默认值为1。
    # @param PtClr 点颜色。默认值为None。
    # @param PtSty 点样式。默认值为None。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SetLn(self, Id, LnClr = "k", LnWd = 1, PtClr = None, PtSty = None):
        LogTr("Enter cOsc.SetLn().")
        self.Ln[Id]["LnClr"] = LnClr
        self.Ln[Id]["LnWd"] = LnWd
        self.Ln[Id]["PtClr"] = PtClr
        self.Ln[Id]["PtSty"] = PtSty
        self.Ln[Id]["Plt"].setData([])
        self.Ln[Id]["Plt"] = self.Pw.plot(pen = pyqtgraph.mkPen(color = LnClr, width = LnWd),
                                          symbolBrush = PtClr, symbol = PtSty)
        self.Ln[Id]["Plt"].setData(self.Ln[Id]["Dat"])
        LogTr("Exit cOsc.SetLn().")

    ##
    # @brief 开关Line显示。
    # @details 无
    # @param self 对象指针。
    # @param Id Line ID编号。
    # @param Sw 开关。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SwLn(self, Id, Sw):
        LogTr("Enter cOsc.SwLn().")
        self.Ln[Id]["Sw"] = Sw

        if Sw == True:
            self.Ln[Id]["Plt"].setData(self.Ln[Id]["Dat"])
        else:
            self.Ln[Id]["Plt"].setData([])
        LogTr("Exit cOsc.SwLn().")

    ##
    # @brief 设置网格属性。
    # @details 无
    # @param self 对象指针。
    # @param SwX 纵向网格显示开关。
    # @arg True 有效。
    # @arg False 无效。
    # @param SwY 横向网格显示开关。
    # @arg True 有效。
    # @arg False 无效。
    # @param Thk 网格线粗细。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SetGrid(self, SwX = False, SwY = False, Thk = 0.1):
        LogTr("Enter cOsc.SetGrid().")
        self.Pw.showGrid(x = SwX, y = SwY, alpha = Thk)
        LogTr("Exit cOsc.SetGrid().")

    ##
    # @brief 设置示波器Label。
    # @details 无
    # @param self 对象指针。
    # @param Ax Label位置。
    # @param Str 显示字符串。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SetLbl(self, Ax, Str):
        LogTr("Enter cOsc.SetLbl().")
        self.Pw.setLabel(axis = Ax, text = Str)
        LogTr("Exit cOsc.SetLbl().")

    ##
    # @brief 采集数据。
    # @details 将采集的数据添加到示波器中显示。如果Id不存在则新建。在曲线之后新增点。
    # @param self 对象指针。
    # @param Dat 待处理数据，为字典型。
    # @return 无
    # @note 无
    # @attention 无
    #
    def CollDat(self, Dat):
        LogTr("Enter cOsc.CollDat().")
        for Id in Dat:
            if Id in self.Ln:
                for Val in Dat[Id]:
                    self.ApdPt(Id, Val)
            else:
                self.AddLn(Id)

                for Val in Dat[Id]:
                    self.ApdPt(Id, Val)
        LogTr("Exit cOsc.CollDat().")
