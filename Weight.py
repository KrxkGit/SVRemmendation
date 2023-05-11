# coding=utf-8
"""
统筹所有权重
"""

import User
import Video
import InitWeightMatrix
import ExWeight
import FeedbackWeight


class Weight:
    def __init__(self):
        self.init_weight_obj = InitWeightMatrix.InitWeight
        self.ex_weight_obj = ExWeight.ExtraWeight
        self.fb_weight_obj = FeedbackWeight.FeedbackWeight
