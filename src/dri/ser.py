import serial
import serial.tools.list_ports

class cSer:
    def __init__(self):
        self.Ser = serial.Serial()

        self.BrDict = {"110":110, "300":300, "600":600, "1200":1200, "2400":2400, "4800":4800, "9600":9600,
                            "14400":14400, "19200":19200, "38400":38400, "56000":56000, "57600":57600, "115200":115200,
                            "129000":129000, "230400":230400, "256000":256000, "460800":460800, "500000":500000,
                            "512000":512000, "600000":600000, "750000":750000, "921600":921600, "1000000":1000000,
                            "1500000":1500000, "2000000":2000000}
        self.BySzDict = {"5":serial.FIVEBITS, "6":serial.SIXBITS, "7":serial.SEVENBITS, "8":serial.EIGHTBITS}
        self.ParDict = {"None":serial.PARITY_NONE, "Even":serial.PARITY_EVEN, "Odd":serial.PARITY_ODD, "Mark":serial.PARITY_MARK, "Space":serial.PARITY_SPACE}
        self.StpBitDict = {"1":serial.STOPBITS_ONE, "1.5":serial.STOPBITS_ONE_POINT_FIVE, "2":serial.STOPBITS_TWO}

    def GetCom(self):
        SerLst = list(serial.tools.list_ports.comports())
        ComLst = []

        if len(SerLst) != 0:
            for i in range(len(SerLst)):
                ComLst.append(SerLst[i].device)

        ComLst = list(set(ComLst)) #删除重复元素
        ComLst.sort()
        return ComLst

    def Opn(self, PtInfo):
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

    def Snd(self, Txt):
        self.Ser.write(Txt)

    def Recv(self, ByNum):
        return self.Ser.read(ByNum)

    def Cl(self):
        try:
            self.Ser.close()
        except:
            raise

    def GetRecvCachLen(self):
        return self.Ser.inWaiting()
