import sys
from PySide.QtCore import *
from PySide.QtGui import *
class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,10))
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
            ])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon([
            QPoint(50, 200), QPoint(150,200),QPoint(100,400),
            ])

        p.drawImage(QRect(200,100,320,320),self.rabbit)
        p.end()
class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        Simple_drawing_window.__init__(self)
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,10))
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
            ])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon([
            QPoint(150, 200), QPoint(50,200),QPoint(50,400),
            ])

        
        p.end()
def main():
    app = QApplication(sys.argv)
    m = Simple_drawing_window2()
    m.show()
    return app.exec_()
        
    
        
