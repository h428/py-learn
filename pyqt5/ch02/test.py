from PyQt5.QtCore import QEasingCurve, QPoint, QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Hello", self)
        self.button.move(100, 100)

        # 创建一个位置动画
        self.animation = QPropertyAnimation(self.button, b"pos")
        self.animation.setDuration(1000)
        self.animation.setStartValue(self.button.pos())
        self.animation.setEndValue(QPoint(200, 200))
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

        # 将按钮的 clicked 信号与启动动画的 start 方法绑定
        self.button.clicked.connect(self.animation.start)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())