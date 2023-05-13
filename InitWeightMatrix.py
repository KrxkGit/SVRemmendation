# coding=utf-8
"""
根据用户属性获得初始权重
"""
import numpy as np
import GlobalVariable


# 根据各属性获得初始权重，注意：初始权重具有全局性
class InitWeight:
    def __init__(self):
        # 权重张量格式(统计性)：[维度1表，维度2表，维度3表]，为加快速度，表用二维数组实现
        self.weight1 = np.zeros((10, 5))
        self.weight2 = np.zeros((10, 2))
        self.weight3 = np.zeros((10, 6))
        self.weightList = [self.weight1, self.weight2, self.weight3]

    # 获得类别权重
    def GetInitWeight(self, category, work_phase, gender, job):
        weight = 1
        weight *= (self.weightList[0])[category][work_phase]
        weight *= (self.weightList[1])[category][gender]
        weight *= (self.weightList[2])[category][job]
        return weight

    # 更新初始权重
    def UpdateInitWeight(self, category, work_phase, gender, job, global_obj: GlobalVariable.GlobalVariable):
        delta = 1 / global_obj.GetTotalUserCount()
        self.weight1[category][work_phase] += delta
        self.weight2[category][gender] += delta
        self.weight3[category][job] += delta
