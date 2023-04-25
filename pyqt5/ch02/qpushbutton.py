import sys
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class QPushButtonDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.button = None
        self.map = {"暂停": ["继续", QIcon("继续.png")],
                    "继续": ["暂停", QIcon("暂停.png")]}
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton Demo")
        self.setGeometry(300, 300, 400, 300)

        vbox = QVBoxLayout()

        # 测试按钮的常规用法：初始状态为继续，展示的本文和图标为暂停
        prev_state_text = "继续"
        button = QPushButton(self.map[prev_state_text][0])  # 创建一个按钮，并设置文本
        button.setIcon(self.map[prev_state_text][1])  # 设置按钮图标
        button.setToolTip("单击播放/暂停播放")  # 设置悬浮提示
        button.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_A))  # 设置 Ctrl + A 为快捷键
        button.clicked.connect(self.buttonClicked)  # 处理按钮的单击事件，此处只是简单演示，后面在介绍信号与槽机制时会详细讲解
        self.button = button

        # 设置按钮样式
        style_button = QPushButton("样式按钮")
        style_button.setStyleSheet(
            "background-color: #4CAF50; color: white; border: none; border-radius: 5px; padding: 10px")
        style_button.clicked.connect(self.styleButtonClicked)

        vbox.addWidget(self.button)  # 按钮添加至布局器
        vbox.addWidget(style_button)
        self.setLayout(vbox)
        self.show()

    def buttonClicked(self):
        """
        按钮单击事件的回调函数，相当于观察者模式中的观察者
        :return: None
        """
        prev_text = self.button.text()  # 使用 button 的 text() 方法读取当前文本
        self.button.setText(self.map[prev_text][0])  # 设置下个状态的文本，使用 setText 设置按钮文本
        self.button.setIcon(self.map[prev_text][1])  # 设置下个状态的图标，使用 setIcon 设置按钮的图标
        self.button.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_A))  # 不知为何处理事件后必须循环设置监听，可能和信号机制有关，后续再研究

    def styleButtonClicked(self):
        sender = self.sender()
        sender.setText("按钮被单击了！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QPushButtonDemo()
    sys.exit(app.exec_())
