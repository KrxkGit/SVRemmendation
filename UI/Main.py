# coding=utf-8

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from uiuser import Ui_user
from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_user()

    ui.setupUi(widget)
    # widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())
