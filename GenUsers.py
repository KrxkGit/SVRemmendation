# coding=utf-8

testVideos = 69  # 用于测试的视频数，也是从文件读取的视频数


def GenUsers():
    print('begin generate users')
    from User import User
    from GlobalVariable import global_obj
    import random
    for i in range(10000):
        user = User(random.randint(0, 4), random.randint(0, 1), random.randint(0, 5), i)
        for j in range(100):
            user.video_list[random.randint(0, 9)].append([random.randint(1, testVideos), 1, 1])
        global_obj.add_user_to_list(user)
    print('generate users done')