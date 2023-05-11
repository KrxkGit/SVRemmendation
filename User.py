"""
属性：
1、用户看过什么视频
    1.1视频id
    1.2该id对应的观看次数
2、用户id(unsigned int)
3、工作阶段
4、性别
5、职业

方法：
1、

"""
import Video


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
    # id
    id: int = None
    # 观看视频总数
    num_of_video: int = 0

    # 已观看视频信息[[电视：[id，次数times,平均停留时长占比ave_len_p],[id,次数，平均停留时长占比ave_len_p]，……],[电影],……]
    video_list = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]

    # 创建新用户
    def __init__(self, work_phase: int, gender: int, job: int, id: int):
        self.work_phase = work_phase
        self.gender = gender
        self.job = job
        self.id = id

    # 观看一个视频，更改已观看视频信息
    # 输入：观看视频、停留时长
    def new_video(self, video: Video, new_len: float):
        # 根据id查找是否已看过，若是，次数加1,；否则新加一个
        self.num_of_video = self.num_of_video + 1
        exist: bool = False  # 判断是否已看过该视频
        for n in self.video_list[video.category]:
            if n[0] == video.id:
                n[1] = n[1] + 1
                n[2] = (n[2] + new_len / video.length) / n[1]
                exist = True
                break
        if not exist:
            self.video_list[video.category].append([video.id, 1, new_len / video.length])

    # 获得一类视频总观看次数
    def num_in_category(self, category) -> int:
        total = 0
        for n in self.video_list[category]:
            total = total + n[1]
        return total

    # 获得对一类视频（电视-娱乐）的总平均停留时间占比
    def stay_p(self, category: int) -> float:
        total = 0.000
        for n in self.video_list[category]:
            total = total + n[2]
        return total / self.num_in_category()

    # 查找某一视频的观看次数并返回
    def isWatched(self, video: Video) -> int:
        for n in self.video_list[video.category]:
            if n[0] == video.id:
                return n[1]
        return 0
