# coding=utf-8
"""
根据用户属性获得初始权重
"""
import random


# 根据各属性获得初始权重，注意：初始权重具有全局性
class InitWeight:
    def __init__(self):
        import numpy as np
        # 权重张量格式(统计性)：[维度1表，维度2表，维度3表]，为加快速度，表用二维数组实现
        self.weight1 = np.ones((10, 5))
        self.weight2 = np.ones((10, 2))
        self.weight3 = np.ones((10, 6))
        self.weightList = [self.weight1, self.weight2, self.weight3]

        # 测试模拟
        for i in range(10):
            for j in range(5):
                self.weight1[i][j] = random.randint(1, 30)

    # 获得类别权重
    def GetInitWeight(self, category, work_phase, gender, job):
        weight = 1
        weight *= (self.weightList[0])[category][work_phase]
        weight *= (self.weightList[1])[category][gender]
        weight *= (self.weightList[2])[category][job]
        return weight

    # 更新初始权重
    def UpdateInitWeight(self, category, work_phase, gender, job):
        from GlobalVariable import global_obj
        base_cut = 0.005  # 将观看数规模缩减后进行比较
        delta = 1 / (global_obj.GetTotalUserCount() * base_cut)
        self.weight1[category][work_phase] += delta
        self.weight2[category][gender] += delta
        self.weight3[category][job] += delta

