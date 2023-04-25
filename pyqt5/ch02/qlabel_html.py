import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class QLabelDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLabel Demo of HTML")
        self.setGeometry(300, 300, 400, 300)

        vbox = QVBoxLayout()

        label = QLabel('<h1 style="color: red;">Hello, <i>world!</i></h1>')
        label.setAlignment(Qt.AlignCenter)
        label.setOpenExternalLinks(True)

        html = open("text.html", "r").read()  # 还可以直接读取 html 文件
        label_new = QLabel(html)
        label_new.setAlignment(Qt.AlignCenter)
        label_new.setOpenExternalLinks(True)

        vbox.addWidget(label)
        vbox.addWidget(label_new)

        self.setLayout(vbox)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QLabelDemo()
    sys.exit(app.exec_())
