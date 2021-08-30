import pyqtgraph

class cOsc:
    def __init__(self, Bg = "w", Fg = "k"):
        self.Ln = {}
        pyqtgraph.setConfigOption("background", Bg)
        pyqtgraph.setConfigOption("foreground", Fg)
        self.Pw = pyqtgraph.PlotWidget(enableAutoRange = True)

    def AddLn(self, Id, LnClr = "k", LnWd = 1, PtClr = "k"):
        self.Ln[Id] = {}
        self.Ln[Id]["LnClr"] = LnClr
        self.Ln[Id]["LnWd"] = LnWd
        self.Ln[Id]["PtClr"] = PtClr
        self.Ln[Id]["Sw"] = True
        self.Ln[Id]["Dat"] = []
        self.Ln[Id]["Plt"] = self.Pw.plot(pen = pyqtgraph.mkPen(color = LnClr, width = LnWd), symbolBrush = PtClr, symbol = "o")

    def DelLn(self, Id):
        self.Ln[Id]["Plt"].setData([])
        del self.Ln[Id]

    def ClrAllLn(self):
        self.Ln.clear()
        self.Pw.clear()

    def SetDat(self, Id, Dat):
        self.Ln[Id]["Dat"] = Dat
        self.Ln[Id]["Plt"].setData(Dat)

    def ApdPt(self, Id, Val):
        self.Ln[Id]["Dat"].append(Val)
        self.Ln[Id]["Plt"].setData(self.Ln[Id]["Dat"])

    def SetLn(self, Id, LnClr = "k", LnWd = 1, PtClr = "k"):
        self.Ln[Id]["LnClr"] = LnClr
        self.Ln[Id]["LnWd"] = LnWd
        self.Ln[Id]["PtClr"] = PtClr
        self.Ln[Id]["Plt"].setData([])
        self.Ln[Id]["Plt"] = self.Pw.plot(pen = pyqtgraph.mkPen(color = LnClr, width = LnWd), symbolBrush = PtClr)
        self.Ln[Id]["Plt"].setData(self.Ln[Id]["Dat"])

    def SwLn(self, Id, Sw):
        self.Ln[Id]["Sw"] = Sw

        if Sw == True:
            self.Ln[Id]["Plt"].setData(self.Ln[Id]["Dat"])
        else:
            self.Ln[Id]["Plt"].setData([])

    def SetGrid(self, SwX = False, SwY = False, Thk = 0.1):
        self.Pw.showGrid(x = SwX, y = SwY, alpha = Thk)

    def SetLbl(self, Ax, Str):
        self.Pw.setLabel(axis = Ax, text = Str)
