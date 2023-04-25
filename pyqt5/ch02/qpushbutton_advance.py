import sys

from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QEasingCurve, QPoint, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class QPushButtonAdvanceDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.button = None
        self.pos_animation = None
        self.size_animation = None
        self.animation_group = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton Advance Demo")
        self.setGeometry(300, 300, 400, 300)

        # 经测试，要演示动画，必须在执行动画时，button 和 animation 要存在，而由于动画是异步执行的，故不能采用局部变量
        self.button = QPushButton("圆形按钮", self)
        self.button.setStyleSheet(
            "background-color: rgba(38, 208, 112, 255); "
            "color: white; "
            "border: none; "
        )
        self.button.resize(100, 100)
        self.button.move(50, 50)  # 设置位置

        self.button.clicked.connect(self.buttonClicked)  # 设置事件处理器
        self.show()

    def buttonClicked(self):
        # 经测试（估计由于动画是异步执行的），animation 必须也是成员变量，如果局部变量无法播放动画

        # 移动按钮位置的动画
        self.pos_animation = QPropertyAnimation(self.button, b'pos')
        self.pos_animation.setDuration(1000)
        self.pos_animation.setStartValue(self.button.pos())
        self.pos_animation.setEndValue(QPoint(200, 200))
        self.pos_animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.pos_animation.start()

        # 变化按钮大小的动画
        self.size_animation = QPropertyAnimation(self.button, b'size')
        self.size_animation.setDuration(1000)
        self.size_animation.setStartValue(QSize(100, 100))
        self.size_animation.setEndValue(QSize(40, 40))

        # 多个动画需要使用 QParallelAnimationGroup 组合起来
        self.animation_group = QParallelAnimationGroup()
        self.animation_group.addAnimation(self.pos_animation)
        self.animation_group.addAnimation(self.size_animation)

        self.animation_group.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QPushButtonAdvanceDemo()
    sys.exit(app.exec_())

