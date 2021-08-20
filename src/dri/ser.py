import serial
import serial.tools.list_ports

class cSer:
    def __init__(self):
        self.Ser = serial.Serial()

    def GetCom(self):
        SerLst = list(serial.tools.list_ports.comports())
        ComLst = []

        if len(SerLst) != 0:
            for i in range(len(SerLst)):
                ComLst.append(SerLst[i].device)

        return ComLst

    def Opn(self):
        pass
