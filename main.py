import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt6.uic import loadUiType
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtCore import Qt, QSize, QRect


UI_Class, BaseClass = loadUiType("UI.ui")


class CanvasWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles_data = []
        self.setMinimumSize(QSize(400, 300))
        self.setStyleSheet("background-color: white;")

    def add_circle(self, x, y, radius):
        self.circles_data = [{'x': x, 'y': y, 'radius': radius}]
        self.update() 

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        background_color = self.palette().color(self.backgroundRole()) 
        painter.fillRect(QRect(0, 0, self.width(), self.height()), QBrush(background_color))

        yellow_color = QColor(255, 255, 0)

        painter.setPen(QPen(Qt.PenStyle.NoPen)) 
        
        painter.setBrush(QBrush(yellow_color, Qt.BrushStyle.SolidPattern))

        for circle in self.circles_data:
            painter.drawEllipse(circle['x'] - circle['radius'],
                                circle['y'] - circle['radius'],
                                circle['radius'] * 2,
                                circle['radius'] * 2)

class MainWindow(QMainWindow, UI_Class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Круги на форме")

        self.canvas = CanvasWidget(self)
        layout = self.centralwidget.layout()
        layout.replaceWidget(self.canvasPlaceholder, self.canvas)
        self.canvasPlaceholder.deleteLater()

        self.pushButton.clicked.connect(self.add_random_circle)

    def add_random_circle(self):
        
        canvas_width = self.canvas.width()
        canvas_height = self.canvas.height()
        
        radius = random.randint(15, 40)

        self.canvas.add_circle(canvas_width // 2, canvas_height // 2, radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
