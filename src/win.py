from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice

class cMainWin:
    def __init__(self):
        MainWinUi = QFile("ui/MainWin.ui")
        MainWinUi.open(QIODevice.ReadOnly)
        self.MainWin = QUiLoader().load(MainWinUi)
        MainWinUi.close()

        self.MainWin.SndPb.clicked.connect(self.PtSnd)

    def show(self):
        self.MainWin.show()

    def PtSnd(self):
        print("PtSnd")
