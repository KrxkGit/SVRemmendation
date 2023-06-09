# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWnd.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import UserLoginWnd
import VideoLoginWnd
import AnalysisWnd


class Ui_MainWnd(object):
    def __init__(self):
        self.widget_analysis = None
        self.widget_user = None
        self.widget_video = None

    def setupUi(self, MainWnd):
        MainWnd.setObjectName("MainWnd")
        MainWnd.resize(346, 370)
        self.UL = QtWidgets.QPushButton(MainWnd)
        self.UL.setGeometry(QtCore.QRect(50, 30, 241, 81))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(22)
        self.UL.setFont(font)
        self.UL.setObjectName("UL")
        self.VL = QtWidgets.QPushButton(MainWnd)
        self.VL.setGeometry(QtCore.QRect(50, 130, 241, 91))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(22)
        self.VL.setFont(font)
        self.VL.setObjectName("VL")
        self.Analysis = QtWidgets.QPushButton(MainWnd)
        self.Analysis.setGeometry(QtCore.QRect(50, 250, 241, 91))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(22)
        self.Analysis.setFont(font)
        self.Analysis.setObjectName("Analysis")

        self.retranslateUi(MainWnd)
        self.UL.clicked.connect(self.UserLogin)  # type: ignore
        self.VL.clicked.connect(self.VideoLogin)  # type: ignore
        self.Analysis.clicked.connect(self.AnalysisFun)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWnd)

    def retranslateUi(self, MainWnd):
        _translate = QtCore.QCoreApplication.translate
        MainWnd.setWindowTitle(_translate("MainWnd", "短视频推荐系统"))
        self.UL.setText(_translate("MainWnd", "用户登录"))
        self.VL.setText(_translate("MainWnd", "视频登录"))
        self.Analysis.setText(_translate("MainWnd", "统计分析"))

    def UserLogin(self):
        self.widget_user = QtWidgets.QWidget()
        self.user_login_wnd = UserLoginWnd.Ui_UserLoginWnd()
        self.user_login_wnd.setupUi(self.widget_user)
        from ReloadIcon import SetWndIcon
        SetWndIcon(self.widget_user)
        self.widget_user.show()

    def VideoLogin(self):
        self.widget_video = QtWidgets.QWidget()
        self.video_login_wnd = VideoLoginWnd.Ui_VideoLoginWnd()
        self.video_login_wnd.setupUi(self.widget_video)
        from ReloadIcon import SetWndIcon
        SetWndIcon(self.widget_video)
        self.widget_video.show()

    def AnalysisFun(self):
        self.widget_analysis = QtWidgets.QWidget()
        self.analysis_wnd = AnalysisWnd.Ui_AnalysisWnd()
        self.analysis_wnd.setupUi(self.widget_analysis)
        from ReloadIcon import SetWndIcon
        SetWndIcon(self.widget_analysis)
        self.widget_analysis.show()
