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
        self.Ln = {}
        pyqtgraph.setConfigOption("background", Bg)
        pyqtgraph.setConfigOption("foreground", Fg)
        self.Pw = pyqtgraph.PlotWidget(enableAutoRange = True)

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
        self.Ln[Id] = {}
        self.Ln[Id]["LnClr"] = LnClr
        self.Ln[Id]["LnWd"] = LnWd
        self.Ln[Id]["PtClr"] = PtClr
        self.Ln[Id]["Sw"] = True
        self.Ln[Id]["Dat"] = []
        self.Ln[Id]["Plt"] = self.Pw.plot(pen = pyqtgraph.mkPen(color = LnClr, width = LnWd),
                                          symbolBrush = PtClr, symbol = PtSty)
        self.Ln[Id]["PtSty"] = PtSty

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
        self.Ln[Id]["Plt"].setData([])
        del self.Ln[Id]

    ##
    # @brief 删除Line对象。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClrAllLn(self):
        self.Ln.clear()
        self.Pw.clear()

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
        self.Ln[Id]["Dat"] = Dat
        self.Ln[Id]["Plt"].setData(Dat)

    ##
    # @brief 设置Line数据。
    # @details Line末尾插入点。
    # @param self 对象指针。
    # @param Id Line ID编号。
    # @param Val 点的值。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ApdPt(self, Id, Val):
        self.Ln[Id]["Dat"].append(Val)
        self.Ln[Id]["Plt"].setData(self.Ln[Id]["Dat"])

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
        self.Ln[Id]["LnClr"] = LnClr
        self.Ln[Id]["LnWd"] = LnWd
        self.Ln[Id]["PtClr"] = PtClr
        self.Ln[Id]["PtSty"] = PtSty
        self.Ln[Id]["Plt"].setData([])
        self.Ln[Id]["Plt"] = self.Pw.plot(pen = pyqtgraph.mkPen(color = LnClr, width = LnWd),
                                          symbolBrush = PtClr, symbol = PtSty)
        self.Ln[Id]["Plt"].setData(self.Ln[Id]["Dat"])

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
        self.Ln[Id]["Sw"] = Sw

        if Sw == True:
            self.Ln[Id]["Plt"].setData(self.Ln[Id]["Dat"])
        else:
            self.Ln[Id]["Plt"].setData([])

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
        self.Pw.showGrid(x = SwX, y = SwY, alpha = Thk)

    def SetLbl(self, Ax, Str):
        self.Pw.setLabel(axis = Ax, text = Str)
