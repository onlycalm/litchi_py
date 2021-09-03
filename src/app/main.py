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
from prot import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    StrFmtProt = cStrFmtProt()
    StrFmtProt.Dec("chA: 1, 2, 3\nchB: 4, 5, 6\n")

    Litchi = cLitchi()
    Litchi.show()

    sys.exit(app.exec_())
