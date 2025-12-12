import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtCore import Qt, QSize, QRect


class MainWindowDesign: 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        self.centralwidget = QWidget(MainWindow)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.canvasPlaceholder = QWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.canvasPlaceholder)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setText("Нарисовать новый круг")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = MainWindow.menuBar()
        self.statusbar = MainWindow.statusBar()


class CanvasWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_circle_data = None 
        self.setMinimumSize(QSize(400, 300))
        self.setStyleSheet("background-color: white;")

    def set_circle(self, x, y, radius, color):
        self.current_circle_data = {'x': x, 'y': y, 'radius': radius, 'color': color}
        self.update() 

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QPen(Qt.PenStyle.NoPen)) 
        
        if self.current_circle_data:
            circle = self.current_circle_data
            painter.setBrush(QBrush(circle['color'], Qt.BrushStyle.SolidPattern))
            painter.drawEllipse(circle['x'] - circle['radius'],
                                circle['y'] - circle['radius'],
                                circle['radius'] * 2,
                                circle['radius'] * 2)

class MainWindow(QMainWindow, MainWindowDesign):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Один Центральный Круг")

        self.canvas = CanvasWidget(self)
        layout = self.centralwidget.layout()
        layout.replaceWidget(self.canvasPlaceholder, self.canvas)
        self.canvasPlaceholder.deleteLater()

        self.pushButton.clicked.connect(self.draw_new_circle)

    def draw_new_circle(self):
        
        canvas_width = self.canvas.width()
        canvas_height = self.canvas.height()
    
        radius = random.randint(15, 100) 
        
        x = canvas_width // 2
        y = canvas_height // 2

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = QColor(r, g, b)
        self.canvas.set_circle(x, y, radius, random_color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
