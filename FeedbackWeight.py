# coding=utf-8
"""
根据反馈参数（点赞量、分享量、评论量占观看量占比）计算全局权重
"""
import GlobalVariable
import Video


def take_watch(video: Video.Video):
    return video.watch


def take_like(video: Video.Video):
    return video.like / video.watch


def take_comment(video: Video.Video):
    return video.comment / video.watch


def take_share(video: Video.Video):
    return video.share / video.watch


def take_result_percent(video: Video.Video):
    weight = (1, 2, 3)  # 权重得分：假设点赞得1分，评论得2分，分享得3分
    return (take_like(video) * weight[0] + take_comment(video) * weight[1] + take_share(video) * weight[
        2]) / video.watch


# 通过给SortKey传递 take_*函数来进行排序，默认传take_result_percent
def SortByFeedBack(global_var: GlobalVariable.GlobalVariable, SortKey):
    video_list = global_var.GlobalVideoList
    video_list.sort(key=SortKey, reverse=True)
