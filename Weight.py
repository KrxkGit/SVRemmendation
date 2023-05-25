# coding=utf-8
"""
统筹所有权重
"""

import ExWeight
import FeedbackWeight
import TimeTest


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

        weight = (self.init_weight_obj.GetInitWeight(video.category, user.work_phase, user.gender, user.job) *
                  self.ex_weight_obj.GetExWeight(video) * fb_weight_obj.take_result_percent())

        if video.hot:
            from GlobalVariable import hot_add_weight_percent
            weight *= (1 + hot_add_weight_percent)
        return weight
