from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice, QDateTime, QTimer
from PySide2.QtWidgets import QAction, QMessageBox, QFileDialog
from PySide2.QtGui import QIcon
from ser import cSer

class cMainWin:
    def __init__(self):
        MainWinUi = QFile("ui/MainWin.ui")
        MainWinUi.open(QIODevice.ReadOnly)
        self.MainWin = QUiLoader().load(MainWinUi)
        MainWinUi.close()

        self.SerDri = cSer()
        self.Tmr = QTimer()

        self.RfrCom()

        self.Tmr.timeout.connect(self.SerTmRecv)
        self.MainWin.AbtAct.triggered.connect(self.ClkAbtAct)
        self.MainWin.RfrComPb.clicked.connect(self.ClkRfrCom)
        self.MainWin.OpnPtPb.clicked.connect(self.ClkOpnPt)
        self.MainWin.SvRecvPb.clicked.connect(self.ClkSvRecv)
        self.MainWin.ClrRecvPb.clicked.connect(self.ClkClrRecv)
        self.MainWin.ClrSndPb.clicked.connect(self.ClkClrSnd)
        self.MainWin.SndPb.clicked.connect(self.ClkPtSnd)

    def show(self):
        self.MainWin.show()

    def SerTmRecv(self):
        RecvLen = self.SerDri.GetRecvCachLen()
        if RecvLen > 0:
            RecvTxt = self.SerDri.Recv(RecvLen)
            self.MainWin.RecvTb.insertPlainText(RecvTxt.decode("Gbk"))

    def ClkAbtAct(self):
        print("About")
        AbtMsgBx = QMessageBox()
        AbtMsgBx.about(self.MainWin, "关于", "内容")

    def ClkRfrCom(self):
        print("RfrCom")
        self.RfrCom()

    def ClkOpnPt(self):
        print("OpnPt")
        if self.SerDri.Ser.is_open == False:
            PtInfo = {"Port":self.MainWin.PtCmb.currentText(),
                      "BaudRate":self.MainWin.BrCmb.currentText(),
                      "ByteSize":self.MainWin.DbCmb.currentText(),
                      "StopBits":self.MainWin.SbCmb.currentText(),
                      "Parity":"None", "Timeout":None,
                      "XOnXOff":False, "RtsCts":False, "Write_Timeout":None,
                      "DsrDtr":False, "Inter_Byte_Timeout":None}
            try:
                self.SerDri.Opn(PtInfo)
            except:
                QMessageBox.critical(self.MainWin, "Error", "串口打开失败")
            else:
                self.Tmr.start(100)
                self.SwPtFrmCmb(False)
                self.MainWin.OpnPtPb.setStyleSheet("background-color:lightblue")
        else:
            try:
                self.SerDri.Cl()
            except:
                QMessageBox.critical(self.MainWin, "Error", "串口打开失败")
            else:
                self.Tmr.stop()
                self.SwPtFrmCmb(True)
                self.MainWin.OpnPtPb.setStyleSheet("background-color:none")

    def ClkSvRecv(self):
        print("SvRecv")
        Tm = QDateTime.currentDateTime()
        FmtTm = Tm.toString('yyMMdd-hhmmss')
        FDlg = QFileDialog(self.MainWin)
        Fpth = FDlg.getSaveFileName(self.MainWin, "保存文件", FmtTm + ".txt")
        if Fpth[0] != '':
            F = open(Fpth[0], 'w')
            F.write(self.MainWin.RecvTb.toPlainText());
            F.close()

    def ClkClrRecv(self):
        print("ClrRecv")
        self.MainWin.RecvTb.clear()

    def ClkClrSnd(self):
        print("ClrSnd")
        self.MainWin.SndPtb.clear()

    def ClkPtSnd(self):
        print("PtSnd")
        if self.SerDri.Ser.is_open == True:
            self.SerDri.Snd(self.MainWin.SndPtb.toPlainText().encode("Gbk"))

    def RfrCom(self):
        ComLst = self.SerDri.GetCom()
        if len(ComLst) != 0:
            ComLst.sort()
            self.MainWin.PtCmb.clear()

            for val in ComLst:
                self.MainWin.PtCmb.addItem(val)

    def SwPtFrmCmb(self, Sw):
        self.MainWin.PtCmb.setEnabled(Sw)
        self.MainWin.BrCmb.setEnabled(Sw)
        self.MainWin.DbCmb.setEnabled(Sw)
        self.MainWin.SbCmb.setEnabled(Sw)
        self.MainWin.ParCmb.setEnabled(Sw)
        self.MainWin.FcCmb.setEnabled(Sw)
        self.MainWin.RfrComPb.setEnabled(Sw)
