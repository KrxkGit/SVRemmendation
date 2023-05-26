import random
import time

import pandas as pd
import TimeTest
from GlobalVariable import global_obj

file_path = '../Data.csv'


def take_uid(video):
    return video.uid


@TimeTest.Krxk_Clock
def ReadFromFile():
    from GenUsers import testVideos
    import threading
    thread_list = []
    data = pd.read_csv(file_path, nrows=testVideos)

    #  分成大组，简单处理，余数进1
    group_size = 2000
    group_num = int(testVideos / group_size) + 1
    for i in range(group_num):
        t = threading.Thread(target=WriteToMemory, args=(data[i * group_size:(i + 1) * group_size],))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()

    global_obj.GlobalVideoList.sort(key=take_uid, reverse=False)  # 升序排列


@TimeTest.Krxk_Clock
def WriteToMemory(data):
    from Video import Video
    for index, row in data.iterrows():
        video = Video(
            category=int(row['category']),
            uid=int(row['ID']),
            length=int(row['length']),
            name=row['name'],
            like=int(row['like']),
            comment=int(row['comment']),
            share=int(row['share']),
            watch=int(row['watch']),
        )
        user_id_list = str(row['user_list']).split(';')

        for user_id in user_id_list:
            if user_id == '':
                continue
            video.new_user(int(user_id))

        global_obj.add_video_to_list(video, True)  # 采用快速模式添加


def ConvertListToStr(ul: list):
    result = str('')
    for item in ul:
        result += str(item) + ';'
    result = result[:-1]
    return result


@TimeTest.Krxk_Clock
def SaveToFile():
    df = pd.DataFrame(columns=['category', 'ID', 'length', 'comment', 'like', 'watch', 'share', 'name', 'user_list'])
    for i, video in enumerate(global_obj.GlobalVideoList):
        df.loc[i + 2] = [video.category, video.uid, video.length, video.comment, video.like, video.watch,
                         video.share, video.name, ConvertListToStr(video.user_list)]

    df.to_csv(file_path + '.bak', encoding='utf-8', index=False)


