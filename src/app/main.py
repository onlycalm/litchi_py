##
# @file main.py
# @brief 入口文件。
# @details 无
# @author Calm
# @date 2021-08-30
# @version v1.0.0
# @copyright Calm
#

import sys
from PySide2.QtWidgets import QApplication
from litchi import cLitchi
import res

from re import *
from prot import *

if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #
    #Litchi = cLitchi()
    #Litchi.show()
    #
    #sys.exit(app.exec_())

    #Str = "chA: 1,2\n\r"
    #end = match(r"(\w+)(\s*):(\s*)(\d(\s*),(\s*))*(\d)(\s*)[\n\r|\r\n|\n]", Str).span()[1]
    #Str = Str[:end]
    #print(Str)
    #Str1 = sub(r"[\n\r|\r\n|\n].*$", "", Str)
    #print(Str1)
    #Id = sub(r":.*$", "", Str1)
    #print(Id)
    #Dat = findall(r"(\d+)", Str1)
    #print(Dat)

    StrFmtProt = cStrFmtProt()
    #print(StrFmtProt.Dec("chA: 1, 2, 3\n\rchB: 4, 5, 6\nchC: 7, 8\r\naa"))
    print(StrFmtProt.Dec("chA: 1, 2, 3\nchB: 4, 5, 6\nchC: 7, 8\r\n"))
