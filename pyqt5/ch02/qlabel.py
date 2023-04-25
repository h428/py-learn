import sys
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLabel Demo")
        self.setGeometry(300, 300, 400, 300)

        vbox = QVBoxLayout()  # 创建一个 QVBoxLayout 布局管理器，后续讲布局时会详细介绍

        # 学习设置 QLabel 的文本内容、字体、颜色、对齐方式和样式
        label1 = QLabel("QLabel 小组件-1")  # 文本内容
        label1.setAlignment(Qt.AlignCenter)  # 对齐方式
        # 字体字号可以使用 setFont 设置，也可以使用样式表设置，如果同时设置经测试会采用样式表的（和代码顺序无关）
        label1.setStyleSheet("color:red; font-size: 22px; font-family: '楷体'")  # 样式
        font = QFont("Courier New", 77, QFont.Bold)  # 字号字体都会被 setStyleSheet 覆盖
        label1.setFont(font)

        # 学习通过 QLabel 展示图像，并设置缩放
        label2 = QLabel()  # 准备一个 QLabel 用于图像展示
        pixmap = QPixmap("image.png")  # 使用 QPixmap 载入图像
        label2.setPixmap(pixmap)  # 设置图像内容
        label2.setFixedSize(150, 150)  # 设置 label2 大小固定
        label2.setScaledContents(True)  # 设置图像为自适应缩放，否则只会展示一部分

        # 学习设置 QLabel 的背景色和提示文本 Tooltip
        label3 = QLabel("鼠标移到这儿！")  # 文本内容
        label3.setStyleSheet("background-color: yellow;")  # 背景色
        label3.setToolTip("鼠标悬停时可以看到这个 Tooltip")  # 提示内容

        # 使用 addWidget 往垂直布局器添加三个控件
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)

        self.setLayout(vbox)  # 使用 setLayout 将布局管理器应用到当前窗口或控件上上
        self.show()  # 使用 show 显示窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLabelDemo()
    sys.exit(app.exec_())
