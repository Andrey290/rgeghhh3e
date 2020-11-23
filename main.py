import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('main.py')
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawer)
        self.flag = False


    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(random.randrange(255), random.randrange(255), random.randrange(255)))
            rudius = int(random.randrange(1000))
            qp.drawArc(0, 0, rudius, rudius, 0 * 16, 360 * 16)
            self.flag = False

    def drawer(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
