import sys
from PySide2.QtWidgets import QApplication
import lichi

if __name__ == "__main__":
    app = QApplication(sys.argv)

    Lichi = lichi.cLichi()
    Lichi.show()

    sys.exit(app.exec_())
