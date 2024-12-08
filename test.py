import sys
import random
from math import sin, cos, pi
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtWidgets import QWidget, QApplication


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()

    def draw(self, status):
        R = random.randint(20, 100)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(QPointF(self.coords_[0], self.coords_[1]), R, R)

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Рисование')

    def mousePressEvent(self, event):
        self.coords_ = [event.pos().x(), event.pos().y()]
        if event.button() == Qt.MouseButton.LeftButton:
            self.status = 1
        elif event.button() == Qt.MouseButton.RightButton:
            self.status = 2
        self.drawf()

    def mouseMoveEvent(self, event):
        self.coords_ = [event.pos().x(), event.pos().y()]

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.status = 3
            self.drawf


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())