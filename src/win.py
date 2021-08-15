from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice

class cMainWin:
    def __init__(self):
        MainWinUi = QFile("ui/MainWin.ui")
        MainWinUi.open(QIODevice.ReadOnly)
        self.MainWin = QUiLoader().load(MainWinUi)
        MainWinUi.close()

        self.MainWin.OpnPtPb.clicked.connect(self.OpnPt)
        self.MainWin.SvRecvPb.clicked.connect(self.SvRecv)
        self.MainWin.ClrRecvPb.clicked.connect(self.ClrRecv)
        self.MainWin.ClrSndPb.clicked.connect(self.ClrSnd)
        self.MainWin.SndPb.clicked.connect(self.PtSnd)

    def show(self):
        self.MainWin.show()

    def OpnPt(self):
        print("OpnPt")

    def SvRecv(self):
        print("SvRecv")

    def ClrRecv(self):
        print("ClrRecv")
        self.MainWin.RecvTb.clear()

    def ClrSnd(self):
        print("ClrSnd")
        self.MainWin.SndPtb.clear()

    def PtSnd(self):
        print("PtSnd")
