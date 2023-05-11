# coding=utf-8
"""
根据反馈参数（点赞量、分享量、评论量占观看量占比）计算全局权重
"""
import GlobalVariable
import Video


class FeedbackWeight:
    def __init__(self, video: Video.Video):
        self.video = video

    def take_watch(self):
        return self.video.watch

    def take_like(self):
        return self.video.like / self.video.watch

    def take_comment(self):
        return self.video.comment / self.video.watch

    def take_share(self):
        return self.video.share / self.video.watch

    # 计算总的反馈权重
    def take_result_percent(self):
        video = self.video
        weight = (1, 2, 3)  # 权重得分：假设点赞得1分，评论得2分，分享得3分
        return (self.take_like(video) * weight[0] + self.take_comment(video) * weight[1] + self.take_share(video) * weight[
            2]) / video.watch

    # 通过给SortKey传递 take_*函数来进行排序，默认传take_result_percent
    def SortByFeedBack(self, global_var: GlobalVariable.GlobalVariable, SortKey):
        video_list = global_var.GlobalVideoList
        video_list.sort(key=SortKey, reverse=True)
