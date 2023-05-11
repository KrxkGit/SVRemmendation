# coding=utf-8
"""
统筹所有权重
"""

import User
import Video
import InitWeightMatrix
import ExWeight
import FeedbackWeight


def CalWeight(init_weight_matrix: InitWeightMatrix.InitWeight, user: User.User, video: Video.Video):
    return init_weight_matrix.GetInitWeight(video)