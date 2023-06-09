# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoLoginWnd.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel


class Ui_VideoLoginWnd(object):
    def setupUi(self, VideoLoginWnd):
        VideoLoginWnd.setObjectName("VideoLoginWnd")
        VideoLoginWnd.resize(881, 701)
        self.label = QtWidgets.QLabel(VideoLoginWnd)
        self.label.setGeometry(QtCore.QRect(30, 50, 221, 31))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(VideoLoginWnd)
        self.textEdit.setGeometry(QtCore.QRect(270, 40, 221, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(font)
        self.Query = QtWidgets.QPushButton(VideoLoginWnd)
        self.Query.setGeometry(QtCore.QRect(520, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(22)
        self.Query.setFont(font)
        self.Query.setObjectName("Query")
        self.listView = QtWidgets.QListView(VideoLoginWnd)
        self.listView.setGeometry(QtCore.QRect(30, 140, 401, 541))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.listView.setFont(font)
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(VideoLoginWnd)
        self.listView_2.setGeometry(QtCore.QRect(450, 140, 401, 541))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.listView_2.setFont(font)
        self.listView_2.setObjectName("listView_2")
        self.label_2 = QtWidgets.QLabel(VideoLoginWnd)
        self.label_2.setGeometry(QtCore.QRect(130, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(VideoLoginWnd)
        self.label_3.setGeometry(QtCore.QRect(590, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Query_2 = QtWidgets.QPushButton(VideoLoginWnd)
        self.Query_2.setGeometry(QtCore.QRect(670, 40, 171, 41))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(22)
        self.Query_2.setFont(font)
        self.Query_2.setObjectName("Query_2")

        self.retranslateUi(VideoLoginWnd)
        self.Query.clicked.connect(self.OnQuery) # type: ignore
        self.Query_2.clicked.connect(self.OnShiftHot)
        QtCore.QMetaObject.connectSlotsByName(VideoLoginWnd)

    def retranslateUi(self, VideoLoginWnd):
        _translate = QtCore.QCoreApplication.translate
        VideoLoginWnd.setWindowTitle(_translate("VideoLoginWnd", "视频查询"))
        self.label.setText(_translate("VideoLoginWnd", "请输入视频 uid:"))
        self.Query.setText(_translate("VideoLoginWnd", "查询"))
        self.label_2.setText(_translate("VideoLoginWnd", "视频统计信息"))
        self.label_3.setText(_translate("VideoLoginWnd", "已观看用户"))
        self.Query_2.setText(_translate("VideoLoginWnd", "切换热点"))

    def OnQuery(self):
        from GlobalVariable import global_obj
        video_uid = int(self.textEdit.toPlainText())
        video = global_obj.GlobalVideoList[video_uid - 1]
        self.cur_video = video  # 保存
        self.model_info = QStringListModel()
        self.listView.setModel(self.model_info)

        self.video_info = ['视频类别： ' + str(video.category), '视频标题: ' + video.name, '播放量： ' + str(video.watch),
                           '点赞量： ' + str(video.like), '评论数： ' + str(video.comment), '分享量：' + str(video.share),
                           '是否热点： ' + str(video.hot), '视频长度： ' + str(video.length)]
        self.model_info.setStringList(self.video_info)

        self.history_users = []
        for user_uid in video.user_list:
            self.history_users.append(str(user_uid))
        self.model_history_users = QStringListModel()
        self.model_history_users.setStringList(self.history_users)
        self.listView_2.setModel(self.model_history_users)

        print('视频查询')

    def OnShiftHot(self):
        if self.cur_video.hot:
            self.cur_video.hot = False
        else:
            self.cur_video.hot = True
        print('热点状态切换，当前状态： ', str(self.cur_video.hot))
