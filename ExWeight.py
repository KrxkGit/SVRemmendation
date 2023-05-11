# coding=utf-8
"""
补充权重：根据用户行为改变
"""
import numpy as np
import User


# 观看历史类别权重：

class ExtraWeight:
    def __init__(self):
        self.exWeightList = np.empty(10, dtype=float)

    def GenExWeight(self, user: User.User):
        for category in range(10):
            self.exWeightList[category] = user.stay_p(category)
            self.exWeightList /= self.exWeightList.sum()
