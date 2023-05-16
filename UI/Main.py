# coding=utf-8

import sys
from PyQt5 import QtWidgets
import MainWnd


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    main_wnd = MainWnd.Ui_MainWnd()
    main_wnd.setupUi(widget)
    widget.show()
    from ReloadIcon import SetWndIcon
    SetWndIcon(widget)  # 增加icon图标
    sys.exit(app.exec_())
