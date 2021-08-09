from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice

class cLitchi:
    def __init__(self):
        MainWinUi = QFile("ui/MainWin.ui")         #要加载的ui文件
        MainWinUi.open(QIODevice.ReadOnly)
        self.MainWin = QUiLoader().load(MainWinUi) #加载UI设计
        MainWinUi.close()

    def show(self):
        self.MainWin.show()
