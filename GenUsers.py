# coding=utf-8
import TimeTest
from GlobalVariable import testVideos
from GlobalVariable import global_obj


def take_uid(user):
    return user.uid


@TimeTest.Krxk_Clock
def GenUsers():
    import threading
    # print('begin generate users')
    total_size = 20000  # 指明要生成的用户数
    group_size = 1000
    group_num = int(total_size / group_size) + 1
    thread_list = []
    for i in range(group_num):
        t = threading.Thread(target=HelpGenUsers, args=(i * group_size, (i + 1) * group_size))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()

    global_obj.GlobalUserList.sort(key=take_uid, reverse=False)
    # print('generate users done')


@TimeTest.Krxk_Clock
def HelpGenUsers(start_uid, end_uid):
    from User import User
    import random
    for i in range(start_uid, end_uid):
        user = User(random.randint(0, 4), random.randint(0, 1), random.randint(0, 5), i)
        for j in range(100):
            user.video_list[random.randint(0, 9)].append([random.randint(1, testVideos), 1, 1])
        global_obj.add_user_to_list(user, True)
