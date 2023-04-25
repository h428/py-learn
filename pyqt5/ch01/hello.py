import sys  # 导入 sys 模块，用于传递命令行参数
from PyQt5.QtWidgets import QApplication, QLabel, QWidget  # PyQt5.QtWidgets 模块包含了许多常用的小部件和控件

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 使用 QApplication 创建一个应用程序实例，其提供了 Qt 的事件循环和其他系统级函数

    window = QWidget()  # 创建窗口：基于 QWidget 类创建窗口
    window.setWindowTitle('Hello, World!')  # setWindowTitle 用于设置窗口标题
    window.setGeometry(100, 100, 280, 80)  # setGeometry 用于设置窗口的位置和大小，入参为 (x, y, w, h)

    # 使用 QLabel 创建一个标签，标签内容使用 HTML 标记
    # 同时使用 parent 参数设置标签为窗口的子控件
    helloMsg = QLabel('<h1>Hello, World!</h1>', parent=window)
    helloMsg.move(60, 15)  # 使用 QLabel 的 move 方法将标签放置在指定位置

    window.show()  # 使用 show 方法显示窗口

    # 使用 sys.exit 方法退出应用程序的应用循环
    # 其中 app.exec_() 方法开始事件循环
    sys.exit(app.exec_())