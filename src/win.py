from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice
from PySide2.QtWidgets import QAction, QMessageBox, QFileDialog
from PySide2.QtGui import QIcon

class cMainWin:
    def __init__(self):
        MainWinUi = QFile("ui/MainWin.ui")
        MainWinUi.open(QIODevice.ReadOnly)
        self.MainWin = QUiLoader().load(MainWinUi)
        MainWinUi.close()

        self.MainWin.AbtAct.triggered.connect(self.AbtAct)
        self.MainWin.OpnPtPb.clicked.connect(self.OpnPt)
        self.MainWin.SvRecvPb.clicked.connect(self.SvRecv)
        self.MainWin.ClrRecvPb.clicked.connect(self.ClrRecv)
        self.MainWin.ClrSndPb.clicked.connect(self.ClrSnd)
        self.MainWin.SndPb.clicked.connect(self.PtSnd)

    def show(self):
        self.MainWin.show()

    def AbtAct(self):
        print("About")
        AbtMsgBx = QMessageBox()
        AbtMsgBx.about(self.MainWin, "关于", "内容")

    def OpnPt(self):
        print("OpnPt")

    def SvRecv(self):
        print("SvRecv")
        FDlg = QFileDialog(self.MainWin)
        QFileDialog.getSaveFileName(self.MainWin, "保存文件", "*.txt")

    def ClrRecv(self):
        print("ClrRecv")
        self.MainWin.RecvTb.clear()

    def ClrSnd(self):
        print("ClrSnd")
        self.MainWin.SndPtb.clear()

    def PtSnd(self):
        print("PtSnd")
