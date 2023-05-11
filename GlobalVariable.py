# coding=utf-8
"""
维护全局变量：全局用户列表、全局视频列表
"""
import numpy as np
import User
import Video


def help_find(id: int, global_list):
    for item in global_list:
        if id == item.id:
            return True
    return False


class GlobalVariable:
    def __init__(self):
        self.GlobalVideoList = []
        self.GlobalUserList = []

    def add_video(self, video: Video.Video):
        if help_find(video.id, self.GlobalVideoList):
            self.GlobalVideoList.append(video)

    def add_user(self, user: User.User):
        if help_find(user.id, self.GlobalUserList):
            self.GlobalUserList.append(user)
