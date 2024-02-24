from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QCheckBox


class OKButton(QPushButton):
    def __init__(self, boxes):
        super().__init__('Order')
        self.boxes = boxes
        self.clicked.connect(self.comd)

    def comd(self):
        for box in self.boxes:
            print(box.text, box.isChecked())


class Checkbox(QCheckBox):
    def __init__(self, btext):
        super().__init__(btext)
        self.text = btext
        if self.text == "Pineapple":
            self.setEnabled(False)


class InitUI(QWidget):
    def __init__(self):
        super().__init__()
        self.names = ["Cheese", "Pepperoni", "Mushrooms", "Sausage", "Peppers", "Pineapple"]
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        boxes = []

        for name in self.names:
            cb = Checkbox(name)
            boxes.append(cb)
            layout.addWidget(cb)

        ok_button = OKButton(boxes)
        layout.addWidget(ok_button)

        self.setLayout(layout)
        self.setWindowTitle('Pizza')
        self.setGeometry(100, 100, 200, 175)
        self.show()


def main():
    app = QApplication([])
    window = InitUI()
    app.exec_()


if __name__ == "__main__":
    main()
