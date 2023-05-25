# coding=utf-8
"""
补充权重：根据用户行为改变
"""


# 观看历史类别权重。由于涉及遍历且重用度较高，保存到用户对象中
class ExtraWeight:
    def __init__(self, user):
        import numpy as np
        self.user = user
        self.exWeightList = np.ones(10, dtype=float)

    def GenExWeight(self):
        user = self.user
        import numpy as np
        from GlobalVariable import global_obj
        category_arr = np.zeros(10, dtype=float)
        for video_uid in user.history_list:
            category_arr[global_obj.GlobalVideoList[video_uid].category] += 1

        temp_sum = category_arr.sum()
        if temp_sum != 0:
            category_arr /= category_arr.sum()

    def GetExWeight(self, video):
        self.GenExWeight()
        return self.exWeightList[video.category]
