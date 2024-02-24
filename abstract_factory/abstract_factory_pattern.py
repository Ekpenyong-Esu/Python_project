import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QLabel, QFrame, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QFont
from abc import ABC, abstractmethod

# Abstract Garden class
class Garden(ABC):
    @abstractmethod
    def get_shade(self): pass
    
    @abstractmethod
    def get_center(self): pass
    
    @abstractmethod
    def get_border(self): pass

# Plant class gives you its name
class Plant:
    def __init__(self, pname):
        self.name = pname  # save name
        
    def get_name(self):
        return self.name

# One of three Garden subclasses
class VeggieGarden(Garden):
    def get_shade(self):
        return Plant("Broccoli")
    
    def get_center(self):
        return Plant("Corn")
    
    def get_border(self):
        return Plant("Peas")

class AnnualGarden(Garden):
    def get_shade(self):
        return Plant("Coleus")
    
    def get_center(self):
        return Plant("Marigold")
    
    def get_border(self):
        return Plant("Alyssum")

class PerennialGarden(Garden):
    def get_shade(self):
        return Plant("Astilbe")
    
    def get_center(self):
        return Plant("Dicentrum")
    
    def get_border(self):
        return Plant("Sedum")

# Outer class that contains the Gardens
class Gardener(QWidget):
    def __init__(self):
        super().__init__()
        self.garden = VeggieGarden()
        self.initUI()

    def set_garden(self, garden):
        self.garden = garden
        self.clear_canvas()

    def clear_canvas(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QColor(0, 0, 0))
        painter.setBrush(QColor(255, 255, 255))
        #painter.drawEllipse(20, 20, 100, 100)

        center_plant = self.garden.get_center().get_name()
        border_plant = self.garden.get_border().get_name()
        shade_plant = self.garden.get_shade().get_name()

        painter.setFont(QFont('Decorative', 10))
        painter.drawText(100, 120, center_plant)
        painter.drawText(75, 180, border_plant)
        painter.drawText(60, 60, shade_plant)

    def initUI(self):
        layout = QVBoxLayout()

        self.setLayout(layout)

        garden_layout = QGridLayout()
        layout.addLayout(garden_layout)

        self.radio_buttons = []

        types_of_gardens = [VeggieGarden, AnnualGarden, PerennialGarden]
        for idx, garden in enumerate(types_of_gardens):
            rb = QRadioButton(garden.__name__, self)
            rb.setChecked(False)
            rb.toggled.connect(lambda state, x=garden: self.set_garden(x()) if state else None)
            garden_layout.addWidget(rb, idx, 0)
            self.radio_buttons.append(rb)

        self.canvas = QLabel(self)
        self.canvas.setMinimumSize(200, 200)
        self.canvas.setFrameShape(QFrame.Box)
        layout.addWidget(self.canvas)

        self.central_button = QPushButton('Central', self)
        self.central_button.clicked.connect(lambda: self.set_garden(self.garden))
        layout.addWidget(self.central_button)

        self.border_button = QPushButton('Border', self)
        self.border_button.clicked.connect(lambda: self.set_garden(self.garden))
        layout.addWidget(self.border_button)

        self.shade_button = QPushButton('Shade', self)
        self.shade_button.clicked.connect(lambda: self.set_garden(self.garden))
        layout.addWidget(self.shade_button)

        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)

        self.clear_canvas()

# Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Garden Planner')
        self.setGeometry(100, 100, 400, 300)

        self.gardener = Gardener()
        self.setCentralWidget(self.gardener)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
