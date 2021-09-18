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
from PySide2.QtCore import QFile, QIODevice, QDateTime, QTimer, Qt
from PySide2.QtWidgets import QAction, QMessageBox, QFileDialog, QTextBrowser, QTreeWidget, QTableWidget
from PySide2.QtGui import QIcon, QColor
from ser import cSer
from grph import cOsc
from log import *
import numpy
from prot import cStrFmtOscProt, cStrFmtLogProt
from thd import *
from detvw import *
from logvw import *

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
        LogTr("Enter cMainWin.__init__().")
        MainWinUi = QFile("ui/MainWin.ui")
        MainWinUi.open(QIODevice.ReadOnly)
        self.MainWin = QUiLoader().load(MainWinUi)
        MainWinUi.close()

        self.SerConnSta = False   #串口连接状态。
        self.StrFmtOscMsgBuf = "" #字符串帧Osc指令消息缓存。
        self.StrFmtLogMsgBuf = "" #字符串帧Osc指令消息缓存。
        self.SerDri = cSer()
        self.Tmr = QTimer()
        self.Osc = cOsc()
        self.DetVw = cDetVw(self.MainWin.DetTw)
        self.LogVw = cLogVw(self.MainWin.LogTw)
        self.StrFmtOscProt = cStrFmtOscProt()
        self.StrFmtLogProt = cStrFmtLogProt()
        self.Thd = cThd(1, "HdlDat", self.WtCb)

        self.LogVw.SetSelBgClr("grey")
        self.MainWin.GrphVl.addWidget(self.Osc.Pw)
        self.RfrCom()

        self.Tmr.timeout.connect(self.SerTmRecv)
        self.DetVw.Tw.clicked.connect(self.ClkDetVw)
        self.LogVw.Tw.clicked.connect(self.ClkLogVw)
        self.MainWin.AbtAct.triggered.connect(self.ClkAbtAct)
        self.MainWin.RfrComPb.clicked.connect(self.ClkRfrCom)
        self.MainWin.OpnPtPb.clicked.connect(self.ClkOpnPt)
        self.MainWin.SvRecvPb.clicked.connect(self.ClkSvRecv)
        self.MainWin.ClrRecvPb.clicked.connect(self.ClkClrRecv)
        self.MainWin.ClrSndPb.clicked.connect(self.ClkClrSnd)
        self.MainWin.SndPb.clicked.connect(self.ClkPtSnd)

        self.Thd.Strt()
        LogTr("Exit cMainWin.__init__().")

    ##
    # @brief 显示窗口。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def show(self):
        LogTr("Enter cMainWin.show().")
        self.MainWin.show()
        LogTr("Exit cMainWin.show().")

    ##
    # @brief 串口定时接收。
    # @details 根据Tmr的时间设置，周期性调用。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SerTmRecv(self):
        LogTr("Enter cMainWin.SerTmRecv().")
        pass
        LogTr("Exit cMainWin.SerTmRecv().")

    ##
    # @brief 点击关于动作。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkAbtAct(self):
        LogTr("Enter cMainWin.ClkAbtAct().")
        AbtMsgBx = QMessageBox()
        AbtMsgBx.about(self.MainWin, "关于", "内容")
        LogTr("Exit cMainWin.ClkAbtAct().")

    ##
    # @brief 点击刷新串口。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkRfrCom(self):
        LogTr("Enter cMainWin.ClkRfrCom().")
        self.RfrCom()
        LogTr("Exit cMainWin.ClkRfrCom().")

    ##
    # @brief 点击打开串口。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkOpnPt(self):
        LogTr("Enter cMainWin.ClkOpnPt().")
        if self.SerDri.GetSwSta() == False:
            PtInfo = {"Port":self.MainWin.PtCmb.currentText(),
                      "BaudRate":self.MainWin.BrCmb.currentText(),
                      "ByteSize":self.MainWin.DbCmb.currentText(),
                      "StopBits":self.MainWin.SbCmb.currentText(),
                      "Parity":"None", "Timeout":None,
                      "XOnXOff":False, "RtsCts":False, "Write_Timeout":None,
                      "DsrDtr":False, "Inter_Byte_Timeout":None}

            self.SerConnSta = True
            try:
                self.SerDri.Opn(PtInfo)
            except:
                QMessageBox.critical(self.MainWin, "Error", "串口打开失败")
            else:
                self.SwPtFrmCmb(False)
                self.MainWin.OpnPtPb.setStyleSheet("background-color:lightblue")
        else:
            self.SerConnSta = False
        LogTr("Exit cMainWin.ClkOpnPt().")

    ##
    # @brief 点击保存接收。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkSvRecv(self):
        LogTr("Enter cMainWin.ClkSvRecv().")
        Tm = QDateTime.currentDateTime()
        FmtTm = Tm.toString('yyMMdd-hhmmss')
        FDlg = QFileDialog(self.MainWin)
        Fpth = FDlg.getSaveFileName(self.MainWin, "保存文件", FmtTm + ".txt")
        if Fpth[0] != '':
            F = open(Fpth[0], 'w')
            F.write(self.MainWin.RecvTb.toPlainText());
            F.close()
        LogTr("Exit cMainWin.ClkSvRecv().")

    ##
    # @brief 点击清空接收。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkClrRecv(self):
        LogTr("Enter cMainWin.ClkClrRecv().")
        self.MainWin.RecvTb.clear()
        LogTr("Exit cMainWin.ClkClrRecv().")

    ##
    # @brief 点击清空发送。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkClrSnd(self):
        LogTr("Enter cMainWin.ClkClrSnd().")
        self.MainWin.SndPtb.clear()
        LogTr("Exit cMainWin.ClkClrSnd().")

    ##
    # @brief 点击串口发送。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkPtSnd(self):
        LogTr("Enter cMainWin.ClkPtSnd().")
        if self.SerDri.GetSwSta() == True:
            self.SerDri.Snd(self.MainWin.SndPtb.toPlainText().encode("Gbk"))
        LogTr("Exit cMainWin.ClkPtSnd().")

    ##
    # @brief 点击Det浏览器。
    # @details 无
    # @param self 对象指针。
    # @param ClkMsg 点击对象。
    # @return 无
    # @note 无
    # @attention 索引从0行0列开始。
    #
    def ClkDetVw(self, ClkMsg):
        LogTr("Enter cMainWin.ClkDetVw().")
        LogDbg(f"ClkMsg.row: {ClkMsg.row()}")
        LogInf(f"{self.DetVw.Tw.currentItem().text(0)} | " +
               f"{self.DetVw.Tw.currentItem().text(1)} | " +
               f"{self.DetVw.Tw.currentItem().text(2)} | " +
               f"{self.DetVw.Tw.currentItem().text(3)}")
        LogTr("Exit cMainWin.ClkDetVw().")

    ##
    # @brief 点击日志浏览器。
    # @details 无
    # @param self 对象指针。
    # @param ClkMsg 点击对象。
    # @return 无
    # @note 无
    # @attention 索引从0行0列开始。
    #
    def ClkLogVw(self, ClkMsg):
        LogTr("Enter cMainWin.ClkLogVw().")
        LogDbg(f"ClkMsg.row: {ClkMsg.row()}")
        self.MainWin.LogTb.clear()

        for i in range(self.LogVw.GetColAmt()):
            self.MainWin.LogTb.insertPlainText(self.LogVw.GetCell(ClkMsg.row(), i) + " ")
        LogTr("Exit cMainWin.ClkLogVw().")

    ##
    # @brief 辅助线程回调函数。
    # @details 无
    # @param 无
    # @return 无
    # @note 无
    # @attention 无
    #
    def WtCb(self, Id, Nm):
        LogTr("Enter cMainWin.WtCb().")
        if (self.SerConnSta == False) and (self.SerDri.GetSwSta() == True):
            try:
                self.SerDri.Cl()
            except:
                QMessageBox.critical(self.MainWin, "Error", "串口打开失败")
            else:
                self.SwPtFrmCmb(True)
                self.MainWin.OpnPtPb.setStyleSheet("background-color:none")

        if self.SerDri.GetSwSta() == True:
            RecvLen = self.SerDri.GetRecvCachLen()
            if RecvLen > 0:
                RecvTxt = self.SerDri.Recv(RecvLen).decode("Gbk")
                self.MainWin.RecvTb.insertPlainText(RecvTxt)
                self.StrFmtOscMsgBuf += RecvTxt
                self.StrFmtLogMsgBuf += RecvTxt
                StrFmtOscProtRes, self.StrFmtOscMsgBuf = self.StrFmtOscProt.Dec(self.StrFmtOscMsgBuf)
                if StrFmtOscProtRes:
                    self.Osc.CollDat(StrFmtOscProtRes)

                StrFmtLogProtRes, self.StrFmtLogMsgBuf = self.StrFmtLogProt.Dec(self.StrFmtLogMsgBuf)
                if StrFmtLogProtRes:
                    self.AddLogRec(StrFmtLogProtRes)
                    self.LogVw.Tw.scrollToBottom() #添加记录太快无法移动到最底部。

        #self.DetVw.ApdRec(["1", "1", "11", "111"])
        #self.DetVw.ApdRec(["2", "2", "22", "222"])
        #self.DetVw.ApdRec(["3", "3", "33", "333"])
        LogTr("Exit cMainWin.WtCb().")

    ##
    # @brief 刷新Com口。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def RfrCom(self):
        LogTr("Enter cMainWin.RfrCom().")
        ComLst = self.SerDri.GetCom()
        if len(ComLst) != 0:
            self.MainWin.PtCmb.clear()

            for val in ComLst:
                self.MainWin.PtCmb.addItem(val)
        LogTr("Exit cMainWin.RfrCom().")

    ##
    # @brief 开关串口Frame中的组合框。
    # @details 将组合框置灰或激活。
    # @param self 对象指针。
    # @param Sw 开关。
    # @arg True 有效。
    # @arg False 无效。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SwPtFrmCmb(self, Sw):
        LogTr("Enter cMainWin.SwPtFrmCmb().")
        self.MainWin.PtCmb.setEnabled(Sw)
        self.MainWin.BrCmb.setEnabled(Sw)
        self.MainWin.DbCmb.setEnabled(Sw)
        self.MainWin.SbCmb.setEnabled(Sw)
        self.MainWin.ParCmb.setEnabled(Sw)
        self.MainWin.FcCmb.setEnabled(Sw)
        self.MainWin.RfrComPb.setEnabled(Sw)
        LogTr("Exit cMainWin.SwPtFrmCmb().")

    ##
    # @brief 增加Log记录。
    # @details 将Log记录逐条添加到日志及LogVw中。
    # @param self 对象指针。
    # @param Rec Log记录，类型为列表。
    # @return 无
    # @note 无
    # @attention 无
    #
    def AddLogRec(self, Rec):
        for OneRec in Rec:
            time = QDateTime.currentDateTime() #获取当前时间。
            LogInf("[%s] %s" % (OneRec["Lv"], OneRec["Des"]))
            self.LogVw.ApdRec([OneRec["Lv"], time.toString("yyyy-MM-dd hh:mm:ss.zzz"), OneRec["Des"]])
            self.LogVw.HlLogLv(self.LogVw.GetRowAmt() - 1, 0, OneRec["Lv"])
