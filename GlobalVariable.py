# coding=utf-8
"""
维护全局变量：全局用户列表、全局视频列表
"""
import numpy as np
import User
import Video
import InitWeightMatrix


def help_find(id: int, global_list, bToDelete: bool):  # bToDelete 指明在遍历时是否删除该元素，用于提高删除效率
    for item in global_list:
        if id == item.id:
            if bToDelete:
                global_list.remove(item)
            return True
    return False


class GlobalVariable:
    def __init__(self):
        self.GlobalVideoList = []
        self.GlobalUserList = []
        self.InitWeight = InitWeightMatrix.InitWeight()

    def add_video_to_list(self, video: Video.Video):
        if help_find(video.id, self.GlobalVideoList, False):
            self.GlobalVideoList.append(video)

    def add_user_to_list(self, user: User.User):
        if help_find(user.id, self.GlobalUserList, False):
            self.GlobalUserList.append(user)

    def del_video_from_list(self, video: Video.Video):
        if help_find(video.id, self.GlobalVideoList, True):
            return True
        else:
            return False

    def del_user_from_list(self, user: User.User):
        if help_find(user.id, self.GlobalUserList, True):
            return True
        else:
            return False

