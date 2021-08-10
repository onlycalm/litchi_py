import sys
from PySide2.QtWidgets import QApplication
import litchi

if __name__ == "__main__":
    app = QApplication(sys.argv)

    Litchi = litchi.cLitchi()
    Litchi.show()

    sys.exit(app.exec_())
