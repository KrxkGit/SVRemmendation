# coding=utf-8
"""
维护全局变量：全局用户列表、全局视频列表
"""

import InitWeightMatrix


def help_find(id: int, global_list, bToDelete: bool):  # bToDelete 指明在遍历时是否删除该元素，用于提高删除效率
    for item in global_list:
        if id == item.uid:
            if bToDelete:
                global_list.remove(item)
            return True
    return False


class GlobalVariable:
    def __init__(self):
        self.GlobalVideoList = []
        self.GlobalUserList = []
        self.InitWeight = InitWeightMatrix.InitWeight()  # 初始权重具有全局性

    def GetTotalUserCount(self):
        return self.GlobalUserList.count()

    def GetTotalVideoCount(self):
        return self.GlobalVideoList.count()

    def add_video_to_list(self, video):
        if help_find(video.uid, self.GlobalVideoList, False):
            self.GlobalVideoList.append(video)

    def add_user_to_list(self, user):
        if help_find(user.uid, self.GlobalUserList, False):
            self.GlobalUserList.append(user)

    def del_video_from_list(self, video):
        if help_find(video.uid, self.GlobalVideoList, True):
            return True
        else:
            return False

    def del_user_from_list(self, user):
        if help_find(user.uid, self.GlobalUserList, True):
            return True
        else:
            return False


global_obj = GlobalVariable()  # 全局变量
