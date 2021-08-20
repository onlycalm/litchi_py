import sys
from PySide2.QtWidgets import QApplication
from litchi import cLitchi

if __name__ == "__main__":
    app = QApplication(sys.argv)

    Litchi = cLitchi()
    Litchi.show()

    sys.exit(app.exec_())
