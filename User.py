"""
属性：
1、用户看过什么视频
    1.1视频id
    1.2该id对应的观看次数
2、用户id(unsigned int)
3、工作阶段
4、性别
5、职业
"""
import TimeTest
import Weight
from GlobalVariable import global_obj


class User:
    # 工作阶段(维度1)
    # 0-小学生，1-初中生，2-高中生，3-大学生，4-已参加工作
    work_phase: int = None
    # 性别 （维度2）
    # 0-男，1-女
    gender: int = None
    # 职业（维度3）
    # 0-老师，1-学生，2-程序员，3-工程师，4-网络主播，5-其他
    job: int = None
    # uid
    uid: int = None
    # 观看视频总数
    num_of_video: int = 0
    # 权重计算对象
    weight_obj: Weight.Weight

    # 已观看视频信息[[电视：[uid，次数times,平均停留时长占比ave_len_p],[uid,次数，平均停留时长占比ave_len_p]，……],[电影],……]
    video_list = [[], [], [], [], [], [], [], [], [], []]

    # 取代已观看历史结构，其中元素为视频uid

    # 创建新用户
    def __init__(self, work_phase: int, gender: int, job: int, uid: int):
        import numpy as np
        from GlobalVariable import refresh_frequency
        self.work_phase = work_phase
        self.gender = gender
        self.job = job
        self.uid = uid
        self.weight_obj = Weight.Weight(self, global_obj.InitWeight)
        self.temp_play_list = None  # 临时播放列表
        self.to_play_list = np.zeros(refresh_frequency)  # 放置即将播放的视频
        self.history_list = []  # 放置播放历史

    # 观看一个视频，更改已观看视频信息
    # 输入：观看视频、停留时长
    # def new_video(self, video, stay_len: float):
    #     # 根据id查找是否已看过，若是，次数加1,；否则新加一个
    #     self.num_of_video = self.num_of_video + 1
    #     exist: bool = False  # 判断是否已看过该视频
    #     for n in self.video_list[video.category]:
    #         if n[0] == video.uid:
    #             n[1] = n[1] + 1
    #             n[2] = (n[2] + stay_len / video.length) / n[1]
    #             exist = True
    #             break
    #     if not exist:
    #         self.video_list[video.category].append([video.uid, 1, stay_len / video.length])

    # 获得一类视频总观看次数
    # def num_in_category(self, category) -> int:
    #     total = 0
    #     for n in self.video_list[category]:
    #         total = total + n[1]
    #     return total
    #
    # # 获得对一类视频（电视-娱乐）的总平均停留时间占比
    # def stay_percent(self, category: int) -> float:
    #     total = 0.000
    #     for n in self.video_list[category]:
    #         total = total + n[2]
    #     return total / self.num_in_category(category)

    # 查找某一视频的观看次数并返回
    def isWatched(self, video) -> int:
        for n in self.video_list[video.category]:
            if n[0] == video.uid:
                return n[1]
        return 0

    @TimeTest.Krxk_Clock
    def HelpRefreshWeight(self):  # 重新计算权重
        self.temp_play_list = []
        from SortList import VideoListSort
        for video in global_obj.GlobalVideoList:
            weight = self.weight_obj.CalWeight(video)
            self.temp_play_list.append([video.uid, weight])
            if len(self.temp_play_list)>100:
                break
        VideoListSort(self.temp_play_list)

    def RefreshWeight(self):  # 刷新播放列表
        self.to_play_list = None  # 释放内存
        self.to_play_list = self.temp_play_list

    def HelpUpdateInitWeight(self, category):  # 辅助函数
        global_obj.InitWeight.UpdateInitWeight(category, self.work_phase, self.gender, self.job)
