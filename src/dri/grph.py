import pyqtgraph

class cOsc:
    def __init__(self, Bg = "w", Fg = "k"):
        pyqtgraph.setConfigOption("background", Bg)
        pyqtgraph.setConfigOption("foreground", Fg)
        self.Pw = pyqtgraph.PlotWidget(enableAutoRange = True)
        self.LnAmt = 0
        self.Ln = {}

    def AddLn(self):
        if self.LnAmt < 10:
            self.LnAmt += 1
            self.Ln[self.LnAmt] = self.Pw.plot()

    def DelLn(self):
        if self.LnAmt > 0:
            self.LnAmt -= 1

    def ClrLn(self):
        self.Ln = {}
        self.LnAmt = 0

    def SetDat(self, LnNum):
        self.Ln[self.LnAmt].setData([100, 200, 300])
