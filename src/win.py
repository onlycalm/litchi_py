from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice, QDateTime
from PySide2.QtWidgets import QAction, QMessageBox, QFileDialog
from PySide2.QtGui import QIcon

class cMainWin:
    def __init__(self):
        MainWinUi = QFile("ui/MainWin.ui")
        MainWinUi.open(QIODevice.ReadOnly)
        self.MainWin = QUiLoader().load(MainWinUi)
        MainWinUi.close()

        self.MainWin.AbtAct.triggered.connect(self.AbtAct)
        self.MainWin.RfrComPb.clicked.connect(self.RfrCom)
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

    def RfrCom(self):
        print("RfrCom")

    def OpnPt(self):
        print("OpnPt")
        self.MainWin.OpnPtPb.setStyleSheet("background-color:lightgreen")
        self.MainWin.OpnPtPb.setText("关闭串口")

    def SvRecv(self):
        print("SvRecv")
        Tm = QDateTime.currentDateTime()
        FmtTm = Tm.toString('yyMMdd-hhmmss')
        FDlg = QFileDialog(self.MainWin)
        Fpth = FDlg.getSaveFileName(self.MainWin, "保存文件", FmtTm + ".txt")
        if Fpth[0] != '':
            F = open(Fpth[0], 'w')
            F.write(self.MainWin.RecvTb.toPlainText());
            F.close()

    def ClrRecv(self):
        print("ClrRecv")
        self.MainWin.RecvTb.clear()

    def ClrSnd(self):
        print("ClrSnd")
        self.MainWin.SndPtb.clear()

    def PtSnd(self):
        print("PtSnd")
