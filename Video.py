"""
属性：
1、视频被什么用户看过
    1.1用户id
    1.2该id对应的次数
    1.3用户停留时间长度占总长占比
2、视频分类：
    电视、电影、鬼畜、生活、时尚、数码、舞蹈、音乐、游戏、娱乐
3、视频标题
4、视频id
5、今日热点
6、视频长度
7、点赞数
8、评论数
9、分享数
"""


class Video:
    # 视频类别:0-9，分别对应电视、电影，……
    category: int = None
    # 视频id
    uid: int = None
    # 视频时长
    length: float = None
    # 视频标题
    name: str = None

    # 点赞数
    like: int = 0
    # 评论数
    comment: int = 0
    # 分享数
    share: int = 0
    # 观看数
    watch: int = 0
    # 今日热点(0-否，1-是) 或者热度分级？
    hot: int = 0
    # 已观看用户信息[[id，次数times，平均停留时长占比ave_len_p],[],……]
    user_list = []

    # 创建新视频
    def __init__(self, category: int, uid: int, length: float, name: str, watch: int, like: int, comment: int,
                 share: int):
        self.category = category
        self.uid = uid
        self.length = length
        self.name = name
        self.feedback_weight = None
        self.hot = False
        self.watch = watch
        self.like = like
        self.comment = comment
        self.share = share

    # 判断是否为今日热点(受喜爱程度)并修改
    # def is_hot(self):
    #     if self.watch > 1000:  # 或者还要考虑点赞、评论、分享数？
    #         self.hot = 1

    # 观看一次视频，更改已观看用户信息
    # 输入：观看用户、观看时长
    def new_user(self, user, new_len: float, isLike: bool, isComment: bool, isShare: bool):
        # 根据id查找是否该用户已观看过，若是，次数加1，修改平均停留时长；否则新加
        self.watch = self.watch + 1
        exist: bool = False  # 判断是否已被该用户观看过
        for n in self.user_list:
            if user.uid == n[0]:
                n[1] = n[1] + 1
                n[2] = (n[2] + new_len / self.length) / n[1]
                exist = True
                break
        if not exist:
            self.user_list.append([user.id, 1, new_len / self.length])

        # 其余操作
        # self.is_hot()  # 视频是否变为热点
        # 是否点赞
        if isLike:
            self.like = self.like + 1
        # 是否评论
        if isComment:
            self.comment = self.comment + 1
        # 是否分享
        if isShare:
            self.share = self.share + 1
