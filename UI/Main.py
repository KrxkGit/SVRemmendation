# coding=utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import MainWnd


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    main_wnd = MainWnd.Ui_MainWnd()
    main_wnd.setupUi(widget)
    widget.show()
    widget.setWindowIcon(QIcon('icon.png'))  # 增加icon图标，如果没有图片可以没有这句
    sys.exit(app.exec_())
