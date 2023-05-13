# coding=utf-8
"""
补充权重：根据用户行为改变
"""


# 观看历史类别权重。由于涉及遍历且重用度较高，保存到用户对象中
class ExtraWeight:
    def __init__(self, user):
        import numpy as np
        self.user = user
        self.exWeightList = np.zeros(10, dtype=float)

    def GenExWeight(self):
        user = self.user
        for category in range(10):
            self.exWeightList[category] = user.stay_p(category)
            self.exWeightList /= self.exWeightList.sum()

    def GetExWeight(self, video):
        return self.exWeightList[video.category]

