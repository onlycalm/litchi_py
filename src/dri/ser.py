##
# @file ser.py
# @brief 串口模块。
# @details 无
# @author Calm
# @date 2021-09-01
# @version v1.0.0
# @copyright Calm
#

import serial
import serial.tools.list_ports
from log import *

##
# @class cSer
# @brief 串口类。
# @details 无
# @note 无
# @attention 无
#
class cSer:
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self):
        LogTr("Enter cLogVw.__init__().")
        self.Ser = serial.Serial()

        self.BrDict = {"110":110, "300":300, "600":600, "1200":1200, "2400":2400, "4800":4800, "9600":9600,
                            "14400":14400, "19200":19200, "38400":38400, "56000":56000, "57600":57600, "115200":115200,
                            "129000":129000, "230400":230400, "256000":256000, "460800":460800, "500000":500000,
                            "512000":512000, "600000":600000, "750000":750000, "921600":921600, "1000000":1000000,
                            "1500000":1500000, "2000000":2000000}
        self.BySzDict = {"5":serial.FIVEBITS, "6":serial.SIXBITS, "7":serial.SEVENBITS, "8":serial.EIGHTBITS}
        self.ParDict = {"None":serial.PARITY_NONE, "Even":serial.PARITY_EVEN, "Odd":serial.PARITY_ODD, "Mark":serial.PARITY_MARK, "Space":serial.PARITY_SPACE}
        self.StpBitDict = {"1":serial.STOPBITS_ONE, "1.5":serial.STOPBITS_ONE_POINT_FIVE, "2":serial.STOPBITS_TWO}
        LogTr("Exit cLogVw.__init__().")

    ##
    # @brief 获取Com口信息。
    # @details 无
    # @param self 对象指针。
    # @return 类型为列表，为检测到的Com口。
    # @note 无
    # @attention 无
    #
    def GetCom(self):
        LogTr("Enter cLogVw.GetCom().")
        SerLst = list(serial.tools.list_ports.comports())
        ComLst = []

        if len(SerLst) != 0:
            for i in range(len(SerLst)):
                ComLst.append(SerLst[i].device)

        ComLst = list(set(ComLst)) #删除重复元素
        ComLst.sort()

        LogTr("Exit cLogVw.GetCom().")
        return ComLst

    ##
    # @brief 打开Com口。
    # @details 无
    # @param self 对象指针。
    # @param PtInfo 类型为字典，含有Com口的配置参数。
    # @return 无
    # @note 带异常检测。
    # @attention 无
    #
    def Opn(self, PtInfo):
        LogTr("Enter cLogVw.Opn().")
        self.Ser.port = PtInfo["Port"]
        self.Ser.baudrate = self.BrDict[PtInfo["BaudRate"]]
        self.Ser.bytesize = self.BySzDict[PtInfo["ByteSize"]]
        self.Ser.stopbits = self.StpBitDict[PtInfo["StopBits"]]
        self.Ser.parity = self.ParDict[PtInfo["Parity"]]
        self.Ser.timeout = PtInfo["Timeout"]
        self.Ser.xonxoff = PtInfo["XOnXOff"]
        self.Ser.rtscts = PtInfo["RtsCts"]
        self.Ser.write_timeout = PtInfo["Write_Timeout"]
        self.Ser.dsrdtr = PtInfo["DsrDtr"]
        self.Ser.inter_byte_timeout = PtInfo["Inter_Byte_Timeout"]

        try:
            self.Ser.open()
        except:
            raise
        LogTr("Exit cLogVw.Opn().")

    ##
    # @brief 发送串口信息。
    # @details 无
    # @param self 对象指针。
    # @param Txt 发送文本。
    # @return 无
    # @note 无
    # @attention 无
    #
    def Snd(self, Txt):
        LogTr("Enter cLogVw.Snd().")
        self.Ser.write(Txt)
        LogTr("Exit cLogVw.Snd().")

    ##
    # @brief 接收串口信息。
    # @details 无
    # @param self 对象指针。
    # @param ByNum 从缓存中接收字节数。
    # @return 类型为字符串，返回读取的指定字节数数据。
    # @note 无
    # @attention 无
    #
    def Recv(self, ByNum):
        LogTr("Enter cLogVw.Recv().")
        LogTr("Exit cLogVw.Recv().")
        return self.Ser.read(ByNum)

    ##
    # @brief 串口关闭。
    # @details 无
    # @param self 对象指针。
    # @param ByNum 从缓存中接收字节数。
    # @return 无
    # @note 带异常检测。
    # @attention 无
    #
    def Cl(self):
        LogTr("Enter cLogVw.Cl().")
        try:
            self.Ser.close()
        except:
            raise
        LogTr("Exit cLogVw.Cl().")

    ##
    # @brief 获取接收缓冲区数据长度。
    # @details 单位是字节。
    # @param self 对象指针。
    # @return 缓冲区数据长度
    # @note 无
    # @attention 无
    #
    def GetRecvCachLen(self):
        LogTr("Enter cLogVw.GetRecvCachLen().")
        LogTr("Exit cLogVw.GetRecvCachLen().")
        return self.Ser.inWaiting()
