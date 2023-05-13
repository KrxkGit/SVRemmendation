# coding=utf-8
"""
统筹所有权重
"""

import ExWeight
import FeedbackWeight


# 作为外壳为每一个用户提供权重计算功能
class Weight:
    def __init__(self, user, InitWeight):
        self.user = user  # 保存用户
        self.init_weight_obj = InitWeight
        self.ex_weight_obj = ExWeight.ExtraWeight(self.user)

    # 计算最终权重，用于权重排序
    def CalWeight(self, video):
        user = self.user
        fb_weight_obj = FeedbackWeight.FeedbackWeight(video)
        return (self.init_weight_obj.GetInitWeight(user.category, user.work_phase, user.gender, user.job) *
                self.ex_weight_obj.GetExWeight(video) * fb_weight_obj.take_result_percent())
