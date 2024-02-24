from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsRectItem, QGraphicsView, QMainWindow


class Rectangle(QGraphicsRectItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, scene):
        scene.addItem(self)


class Square(Rectangle):
    def __init__(self, x, y, width):
        super().__init__(x, y, width, width)

    def draw(self, scene):
        scene.addItem(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        scene = QGraphicsScene(self)
        self.view = QGraphicsView(scene)

        rect1 = Rectangle(30, 10, 120, 80)
        rect1.draw(scene)

        square = Square(200, 50, 60)
        square.draw(scene)

        self.setCentralWidget(self.view)
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('PyQt Example')


def main():
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()


if __name__ == "__main__":
    main()
