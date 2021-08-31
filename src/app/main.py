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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    Litchi = cLitchi()
    Litchi.show()

    sys.exit(app.exec_())
