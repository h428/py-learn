import sys
import HorizontalLayout, VerticalLayout, GridLayout, SpacerAndLine
from PyQt5.QtWidgets import QApplication, QMainWindow


def run_horizontal_layout(window):
    # 创建 ui 对象
    ui = HorizontalLayout.Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(window)


def run_vertical_layout(window):
    # 创建 ui 对象
    ui = VerticalLayout.Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(window)


def run_grid_layout(window):
    # 创建 ui 对象
    ui = GridLayout.Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(window)


def run_spacer_and_line(window):
    ui = SpacerAndLine.Ui_MainWindow()
    ui.setupUi(window)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    run_spacer_and_line(main_window)
    main_window.show()
    sys.exit(app.exec_())
