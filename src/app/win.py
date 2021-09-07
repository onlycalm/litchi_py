##
# @file win.py
# @brief 窗口模块。
# @details 无
# @author Calm
# @date 2021-08-30
# @version v1.0.0
# @copyright Calm
#

from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice, QDateTime, QTimer
from PySide2.QtWidgets import QAction, QMessageBox, QFileDialog
from PySide2.QtGui import QIcon
from ser import cSer
from grph import cOsc
from log import *
import numpy
from prot import cStrFmtProt
from thd import *

##
# @class cMainWin
# @brief Lichi窗口类。
# @details 该类用于构建Lichi的窗口显示和功能。
# @note 无
# @attention 无
#
class cMainWin:
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self):
        MainWinUi = QFile("ui/MainWin.ui")
        MainWinUi.open(QIODevice.ReadOnly)
        self.MainWin = QUiLoader().load(MainWinUi)
        MainWinUi.close()

        self.SerDri = cSer()
        self.Tmr = QTimer()
        self.Osc = cOsc()
        self.StrFmtProt = cStrFmtProt()
        self.Thd = cThd(1, "HdlDat", self.WtCb)
        self.Thd.Strt()

        self.RfrCom()
        self.MainWin.GrphVl.addWidget(self.Osc.Pw)

        self.Tmr.timeout.connect(self.SerTmRecv)
        self.MainWin.AbtAct.triggered.connect(self.ClkAbtAct)
        self.MainWin.RfrComPb.clicked.connect(self.ClkRfrCom)
        self.MainWin.OpnPtPb.clicked.connect(self.ClkOpnPt)
        self.MainWin.SvRecvPb.clicked.connect(self.ClkSvRecv)
        self.MainWin.ClrRecvPb.clicked.connect(self.ClkClrRecv)
        self.MainWin.ClrSndPb.clicked.connect(self.ClkClrSnd)
        self.MainWin.SndPb.clicked.connect(self.ClkPtSnd)

    ##
    # @brief 显示窗口。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def show(self):
        self.MainWin.show()

    ##
    # @brief 串口定时接收。
    # @details 根据Tmr的时间设置，周期性调用。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SerTmRecv(self):
        RecvLen = self.SerDri.GetRecvCachLen()
        if RecvLen > 0:
            RecvTxt = self.SerDri.Recv(RecvLen)
            self.MainWin.RecvTb.insertPlainText(RecvTxt.decode("Gbk"))

    ##
    # @brief 点击关于动作。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkAbtAct(self):
        print("About")
        AbtMsgBx = QMessageBox()
        AbtMsgBx.about(self.MainWin, "关于", "内容")

    ##
    # @brief 点击刷新串口。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkRfrCom(self):
        print("RfrCom")
        self.RfrCom()

    ##
    # @brief 点击打开串口。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
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

    ##
    # @brief 点击保存接收。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
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

    ##
    # @brief 点击清空接收。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkClrRecv(self):
        print("ClrRecv")
        self.MainWin.RecvTb.clear()

    ##
    # @brief 点击清空发送。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkClrSnd(self):
        print("ClrSnd")
        self.MainWin.SndPtb.clear()

    ##
    # @brief 点击串口发送。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkPtSnd(self):
        print("PtSnd")
        if self.SerDri.Ser.is_open == True:
            self.SerDri.Snd(self.MainWin.SndPtb.toPlainText().encode("Gbk"))

    ##
    # @brief 辅助线程回调函数。
    # @details 无
    # @param 无
    # @return 无
    # @note 无
    # @attention 无
    #
    def WtCb(self, Id, Nm):
        #while True:
            Msg = "chA: 1, 2, 3\nchB: 4, 5, 6\r\nchC: 7, 8, 9\n\r"
            Dic, _ = self.StrFmtProt.Dec(Msg)
            self.Osc.CollDat(Dic)

    ##
    # @brief 刷新Com口。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def RfrCom(self):
        ComLst = self.SerDri.GetCom()
        if len(ComLst) != 0:
            self.MainWin.PtCmb.clear()

            for val in ComLst:
                self.MainWin.PtCmb.addItem(val)

    ##
    # @brief 开关串口Frame中的组合框。
    # @details 将组合框置灰或激活
    # @param self 对象指针。
    # @param Sw 开关。
    # @arg True 有效。
    # @arg False 无效。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SwPtFrmCmb(self, Sw):
        self.MainWin.PtCmb.setEnabled(Sw)
        self.MainWin.BrCmb.setEnabled(Sw)
        self.MainWin.DbCmb.setEnabled(Sw)
        self.MainWin.SbCmb.setEnabled(Sw)
        self.MainWin.ParCmb.setEnabled(Sw)
        self.MainWin.FcCmb.setEnabled(Sw)
        self.MainWin.RfrComPb.setEnabled(Sw)
