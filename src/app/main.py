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
from log import *
from prot import *

def main():
    LogTr("Enter main().")
    app = QApplication(sys.argv)

    Litchi = cLitchi()
    Litchi.show()

    sys.exit(app.exec_())
    LogTr("Exit main().")

if __name__ == "__main__":
    main()

    #StrFmtProt = cStrFmtProt()
    #StrFmtProt.Dec("Test\nAAAA\n")
    #StrFmtProt.Dec("Test\n")
    #LogDbg(StrFmtProt.Dec("Test\nAAAA\nBBBB"))
    #LogDbg(StrFmtProt.Dec(""))
    #LogDbg(StrFmtProt.DecInstr("Ch11: 1, 2, 3\n"))
    #LogDbg(StrFmtProt.Dec("Test\nCh11: 1, 2, 3\nChA: 4, 5, 6\nCh11: 7, 8, 9\nhaha"))
