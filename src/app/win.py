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
from PySide2.QtCore import QFile, QIODevice, QDateTime, QTimer, Qt, QObject, Signal
from PySide2.QtWidgets import QAction, QMessageBox, QFileDialog, QTextBrowser, QTreeWidget, QTableWidget, QLabel, QMenu
from PySide2.QtWidgets import QCheckBox
from PySide2.QtGui import QIcon, QColor, QTextCursor
from ser import cSer
from grph import cOsc
from log import *
import numpy
from prot import cStrFmtOscProt, cStrFmtLogProt
from thd import *
from detvw import *
from logvw import *
from led import *

##
# @class cMainWin
# @brief Lichi窗口类。
# @details 该类用于构建Lichi的窗口显示和功能。
# @note 无
# @attention 无
#
class cMainWin(QObject):
    RecvTbSgn = Signal(str)
    LogVwSgn = Signal()

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
        super(cMainWin, self).__init__()
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
        self.CrtLed = cLed(Clr = self.LogVw.LvClr["CRITICAL"])
        self.ErrLed = cLed(Clr = self.LogVw.LvClr["ERROR"])
        self.WrnLed = cLed(Clr = self.LogVw.LvClr["WARNING"])
        self.ScsLed = cLed(Clr = self.LogVw.LvClr["SUCCESS"])
        self.Thd = cThd(1, "HdlDat")

        self.LogVwSgn.connect(self.RfrLogVw)
        self.RecvTbSgn.connect(self.RfrRecvTb)
        self.MainWin.statusbar.addWidget(self.CrtLed.Lbl)
        self.MainWin.statusbar.addWidget(self.ErrLed.Lbl)
        self.MainWin.statusbar.addWidget(self.WrnLed.Lbl)
        self.MainWin.statusbar.addWidget(self.ScsLed.Lbl)
        self.MainWin.statusbar.setSizeGripEnabled(False)                       #取消窗口右下角三角符。
        self.MainWin.setFixedSize(self.MainWin.width(), self.MainWin.height()) #禁用窗口拉伸及最大化按钮。
        self.Root = QTreeWidgetItem()
        self.Child = QTreeWidgetItem()
        self.Child1 = QTreeWidgetItem()
        self.Root.setText(0, "父节点")
        self.Child.setText(0, "子节点")
        self.Child1.setText(0, "子节点")
        self.Root.addChild(self.Child)
        self.Child.addChild(self.Child1)
        self.DetVw.Tw.addTopLevelItem(self.Root)
        self.LogVw.SetSelBgClr("grey")
        self.MainWin.GrphVl.addWidget(self.Osc.Pw)
        self.RfrCom()

        self.Thd.ConnCb(self.WtCb)
        self.Tmr.timeout.connect(self.HdlPrdTsk)
        self.DetVw.Tw.clicked.connect(self.ClkDetVw)
        self.LogVw.Tw.clicked.connect(self.ClkLogVw)
        self.MainWin.AbtAct.triggered.connect(self.ClkAbtAct)
        self.MainWin.RfrComPb.clicked.connect(self.ClkRfrCom)
        self.MainWin.OpnPtPb.clicked.connect(self.ClkOpnPt)
        self.MainWin.SvRecvPb.clicked.connect(self.ClkSvRecv)
        self.MainWin.ClrRecvPb.clicked.connect(self.ClkClrRecv)
        self.MainWin.ClrSndPb.clicked.connect(self.ClkClrSnd)
        self.MainWin.SndPb.clicked.connect(self.ClkPtSnd)
        self.MainWin.ScrLogCrtChk.clicked.connect(self.ClkScrLogCrt)
        self.MainWin.ScrLogErrChk.clicked.connect(self.ClkScrLogErr)
        self.MainWin.ScrLogWrnChk.clicked.connect(self.ClkScrLogWrn)
        self.MainWin.ScrLogScsChk.clicked.connect(self.ClkScrLogScs)
        self.MainWin.ScrLogInfChk.clicked.connect(self.ClkScrLogInf)
        self.MainWin.ScrLogDbgChk.clicked.connect(self.ClkScrLogDbg)
        self.MainWin.ScrLogTrChk.clicked.connect(self.ClkScrLogTr)
        self.MainWin.ScrLogAllChk.clicked.connect(self.ClkScrLogAll)
        self.MainWin.ClrLogPb.clicked.connect(self.ClkClrLog)
        self.MainWin.LdLogPb.clicked.connect(self.ClkLdLog)

        self.Tmr.start(100)
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
    # @brief 定时处理。
    # @details 根据Tmr的时间设置，周期性调用。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def HdlPrdTsk(self):
        LogTr("Enter cMainWin.HdlPrdTsk().")
        self.SetLogSta(self.LogVw.LvCnt["CRITICAL"], self.LogVw.LvCnt["ERROR"],
                    self.LogVw.LvCnt["WARNING"], self.LogVw.LvCnt["SUCCESS"])
        LogTr("Exit cMainWin.HdlPrdTsk().")

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
        FPth = FDlg.getSaveFileName(self.MainWin, "保存文件", FmtTm + ".txt", filter = "*.txt")
        if FPth[0] != "":
            F = open(FPth[0], 'w')
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
        SelRowNum = ClkMsg.row()

        #if self.LogVw.GetCell(SelRowNum, 0) in self.LogVw.LvClr:
        #    self.LogVw.SetSelBgClr(self.LogVw.LvClr[self.LogVw.GetCell(SelRowNum, 0)])
        #else:
        #    self.LogVw.SetSelBgClr("grey")

        SelRowStr = ""
        for i in range(self.LogVw.GetColAmt()):
            SelRowStr += self.LogVw.GetCell(SelRowNum, i) + " "
        self.MainWin.LogTb.setPlainText(SelRowStr)
        LogInf(f"SelRowNum: {SelRowNum}. {self.MainWin.LogTb.document().toPlainText()}")
        LogTr("Exit cMainWin.ClkLogVw().")

    ##
    # @brief CheckBox点击事件。
    # @details 无。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无。
    #
    def ClkScrLogCrt(self):
        LogTr("Enter cMainWin.ClkScrLogCrt().")
        if self.MainWin.ScrLogCrtChk.isChecked():
            if self.IsSelAllScrLogChk():
                self.MainWin.ScrLogAllChk.setChecked(True)
        else:
            self.MainWin.ScrLogAllChk.setChecked(False)

        self.FltLog()
        LogTr("Exit cMainWin.ClkScrLogCrt().")

    ##
    # @brief CheckBox点击事件。
    # @details 无。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无。
    #
    def ClkScrLogErr(self):
        LogTr("Enter cMainWin.ClkScrLogErr().")
        if self.MainWin.ScrLogErrChk.isChecked():
            if self.IsSelAllScrLogChk():
                self.MainWin.ScrLogAllChk.setChecked(True)
        else:
            self.MainWin.ScrLogAllChk.setChecked(False)

        self.FltLog()
        LogTr("Exit cMainWin.ClkScrLogErr().")

    ##
    # @brief CheckBox点击事件。
    # @details 无。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无。
    #
    def ClkScrLogWrn(self):
        LogTr("Enter cMainWin.ClkScrLogWrn().")
        if self.MainWin.ScrLogWrnChk.isChecked():
            if self.IsSelAllScrLogChk():
                self.MainWin.ScrLogAllChk.setChecked(True)
        else:
            self.MainWin.ScrLogAllChk.setChecked(False)

        self.FltLog()
        LogTr("Exit cMainWin.ClkScrLogWrn().")

    ##
    # @brief CheckBox点击事件。
    # @details 无。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无。
    #
    def ClkScrLogScs(self):
        LogTr("Enter cMainWin.ClkScrLogScs().")
        if self.MainWin.ScrLogScsChk.isChecked():
            if self.IsSelAllScrLogChk():
                self.MainWin.ScrLogAllChk.setChecked(True)
        else:
            self.MainWin.ScrLogAllChk.setChecked(False)

        self.FltLog()
        LogTr("Exit cMainWin.ClkScrLogScs().")

    ##
    # @brief CheckBox点击事件。
    # @details 无。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无。
    #
    def ClkScrLogInf(self):
        LogTr("Enter cMainWin.ClkScrLogInf().")
        if self.MainWin.ScrLogInfChk.isChecked():
            if self.IsSelAllScrLogChk():
                self.MainWin.ScrLogAllChk.setChecked(True)
        else:
            self.MainWin.ScrLogAllChk.setChecked(False)

        self.FltLog()
        LogTr("Exit cMainWin.ClkScrLogInf().")

    ##
    # @brief CheckBox点击事件。
    # @details 无。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无。
    #
    def ClkScrLogDbg(self):
        LogTr("Enter cMainWin.ClkScrLogDbg().")
        if self.MainWin.ScrLogDbgChk.isChecked():
            if self.IsSelAllScrLogChk():
                self.MainWin.ScrLogAllChk.setChecked(True)
        else:
            self.MainWin.ScrLogAllChk.setChecked(False)

        self.FltLog()
        LogTr("Exit cMainWin.ClkScrLogDbg().")

    ##
    # @brief CheckBox点击事件。
    # @details 无。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无。
    #
    def ClkScrLogTr(self):
        LogTr("Enter cMainWin.ClkScrLogTr().")
        if self.MainWin.ScrLogTrChk.isChecked():
            if self.IsSelAllScrLogChk():
                self.MainWin.ScrLogAllChk.setChecked(True)
        else:
            self.MainWin.ScrLogAllChk.setChecked(False)

        self.FltLog()
        LogTr("Exit cMainWin.ClkScrLogTr().")

    ##
    # @brief CheckBox点击事件。
    # @details 选中时触发同时选中所有复选框。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 与其他复选框互斥。
    #
    def ClkScrLogAll(self):
        LogTr("Enter cMainWin.ClkScrLogAll().")
        if self.MainWin.ScrLogAllChk.isChecked():
            self.SelAllScrLogChk(True)
        else:
            if self.IsSelAllScrLogChk():
                self.SelAllScrLogChk(False)

        self.FltLog()
        LogTr("Exit cMainWin.ClkScrLogAll().")

    ##
    # @brief 加载Log点击事件。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkLdLog(self):
        LogTr("Enter cMainWin.ClkLdLog().")
        FDlg = QFileDialog(self.MainWin)
        FPth = FDlg.getOpenFileName(self.MainWin, "加载Log", filter = "*.log")
        if FPth[0] != "":
            self.SelAllScrLogChk(True)
            self.ClkClrLog()
            self.LogVw.LdLog(FPth[0])
        LogTr("Exit cMainWin.ClkLdLog().")

    ##
    # @brief 清空Log点击事件。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClkClrLog(self):
        LogTr("Enter cMainWin.ClkClrLog().")
        self.LogVw.Clr()
        self.MainWin.LogTb.clear()
        LogTr("Exit cMainWin.ClkClrLog().")

    ##
    # @brief 是否选中了所有筛选Log复选框。
    # @details 无
    # @param 无
    # @return 是否全选。
    # @note 无
    # @attention 无
    #
    def IsSelAllScrLogChk(self):
        LogTr("Enter cMainWin.IsSelAllScrLogChk().")
        Rtn = False

        if self.MainWin.ScrLogCrtChk.isChecked() and \
           self.MainWin.ScrLogErrChk.isChecked() and \
           self.MainWin.ScrLogWrnChk.isChecked() and \
           self.MainWin.ScrLogScsChk.isChecked() and \
           self.MainWin.ScrLogInfChk.isChecked() and \
           self.MainWin.ScrLogDbgChk.isChecked() and \
           self.MainWin.ScrLogTrChk.isChecked():
           Rtn = True
        else:
           Rtn = False

        LogTr("Exit cMainWin.IsSelAllScrLogChk().")
        return Rtn

    ##
    # @brief 选中了所有筛选Log复选框。
    # @details 无
    # @param 无
    # @return 是否全选。
    # @note 无
    # @attention 无
    #
    def SelAllScrLogChk(self, Sw):
        if Sw:
            self.MainWin.ScrLogCrtChk.setChecked(True)
            self.MainWin.ScrLogErrChk.setChecked(True)
            self.MainWin.ScrLogWrnChk.setChecked(True)
            self.MainWin.ScrLogScsChk.setChecked(True)
            self.MainWin.ScrLogInfChk.setChecked(True)
            self.MainWin.ScrLogDbgChk.setChecked(True)
            self.MainWin.ScrLogTrChk.setChecked(True)
            self.MainWin.ScrLogAllChk.setChecked(True)
        else:
            self.MainWin.ScrLogCrtChk.setChecked(False)
            self.MainWin.ScrLogErrChk.setChecked(False)
            self.MainWin.ScrLogWrnChk.setChecked(False)
            self.MainWin.ScrLogScsChk.setChecked(False)
            self.MainWin.ScrLogInfChk.setChecked(False)
            self.MainWin.ScrLogDbgChk.setChecked(False)
            self.MainWin.ScrLogTrChk.setChecked(False)
            self.MainWin.ScrLogAllChk.setChecked(False)

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
                RecvStr = self.SerDri.Recv(RecvLen).decode("Gbk")
                self.RecvTbSgn.emit(RecvStr)
                self.StrFmtOscMsgBuf += RecvStr
                self.StrFmtLogMsgBuf += RecvStr
                StrFmtOscProtRes, self.StrFmtOscMsgBuf = self.StrFmtOscProt.Dec(self.StrFmtOscMsgBuf)
                if StrFmtOscProtRes:
                    self.Osc.CollDat(StrFmtOscProtRes)

                StrFmtLogProtRes, self.StrFmtLogMsgBuf = self.StrFmtLogProt.Dec(self.StrFmtLogMsgBuf)
                if StrFmtLogProtRes:
                    self.AddLogRec(StrFmtLogProtRes)
                    self.LogVwSgn.emit()

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
        LogTr("Enter cMainWin.AddLogRec().")
        for OneRec in Rec:
            time = QDateTime.currentDateTime() #获取当前时间。
            LogInf("[%s] %s" % (OneRec["Lv"], OneRec["Des"]))
            self.LogVw.ApdRec([OneRec["Lv"], time.toString("yyyy-MM-dd hh:mm:ss.zzz"), OneRec["Des"]])
            self.LogVw.HlLogLv(self.LogVw.GetRowAmt() - 1, 0, OneRec["Lv"])
            self.LogVw.CntLog(OneRec["Lv"])
        LogTr("Exit cMainWin.AddLogRec().")

    ##
    # @brief 设置Log状态。
    # @details 设置状态栏的显示内容。
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def SetLogSta(self, CrtLogCnt, ErrLogCnt, WrnLogCnt, ScsLogCnt):
        LogTr("Enter cMainWin.SetLogSta().")
        self.CrtLed.SetStr("CRT:%-5d" % (CrtLogCnt))
        self.ErrLed.SetStr("ERR:%-5d" % (ErrLogCnt))
        self.WrnLed.SetStr("WRN:%-5d" % (WrnLogCnt))
        self.ScsLed.SetStr("SCS:%-5d" % (ScsLogCnt))

        if CrtLogCnt != 0:
            self.CrtLed.Sw(True)
        else:
            self.CrtLed.Sw(False)

        if ErrLogCnt != 0:
            self.ErrLed.Sw(True)
        else:
            self.ErrLed.Sw(False)

        if WrnLogCnt != 0:
            self.WrnLed.Sw(True)
        else:
            self.WrnLed.Sw(False)

        if ScsLogCnt != 0:
            self.ScsLed.Sw(True)
        else:
            self.ScsLed.Sw(False)
        LogTr("Exit cMainWin.SetLogSta().")

    ##
    # @brief 刷新LogVw控件。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def RfrLogVw(self):
        LogTr("Enter cMainWin.RfrLogVw().")
        self.LogVw.Tw.scrollToBottom() #子线程中调用不能到达底部。
        LogTr("Exit cMainWin.RfrLogVw().")

    ##
    # @brief 刷新RecvTb控件。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def RfrRecvTb(self, RecvStr):
        LogTr("Enter cMainWin.RfrRecvTb().")
        self.MainWin.RecvTb.moveCursor(self.MainWin.RecvTb.textCursor().End) #光标移动到末后插入。
        self.MainWin.RecvTb.insertPlainText(RecvStr)                         #append会插入换行。
        ScrBar = self.MainWin.RecvTb.verticalScrollBar()
        ScrBar.setValue(ScrBar.maximum())
        LogTr("Exit cMainWin.RfrRecvTb().")

    ##
    # @brief 对LogVw进行Log筛选。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def FltLog(self):
        LogTr("Enter cMainWin.FltLogLv().")
        SelLogLv = []
        if self.MainWin.ScrLogCrtChk.isChecked():
            SelLogLv.append("CRITICAL")

        if self.MainWin.ScrLogErrChk.isChecked():
            SelLogLv.append("ERROR")

        if self.MainWin.ScrLogWrnChk.isChecked():
            SelLogLv.append("WARNING")

        if self.MainWin.ScrLogScsChk.isChecked():
            SelLogLv.append("SUCCESS")

        if self.MainWin.ScrLogInfChk.isChecked():
            SelLogLv.append("INFO")

        if self.MainWin.ScrLogDbgChk.isChecked():
            SelLogLv.append("DEBUG")

        if self.MainWin.ScrLogTrChk.isChecked():
            SelLogLv.append("TRACE")

        self.LogVw.FltLog(SelLogLv)
        LogTr("Exit cMainWin.FltLogLv().")
