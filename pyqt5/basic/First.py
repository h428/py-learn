import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建 QApplication 实例
    win = QWidget()  # 创建一个窗口
    win.resize(300, 150)  # 主区域大小 （300, 150）（不包括菜单栏）
    win.move(300, 300)  # 设置窗口位置，距离左上角 （300, 300）
    win.setWindowTitle("第一个基于PyQT5的应用")  # 设置窗口标题
    win.show()  # 显示窗口
    sys.exit(app.exec_())  # 进入程序主循环，并通过 exit 确保主循环安全结束

