import pandas as pd
import TimeTest
from GlobalVariable import global_obj

file_path = '../Data.csv'


def take_uid(video):
    return video.uid


@TimeTest.KrxkClock
def ReadFromFile():
    from GenUsers import testVideos
    import threading
    thread_list = []
    data = pd.read_csv(file_path, nrows=testVideos)
    for i in range(11):
        t = threading.Thread(target=WriteToMemory, args=(data[i * 10000:(i + 1) * 10000 + 1],))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()

    global_obj.GlobalVideoList.sort(key=take_uid, reverse=False)  # 升序排列


@TimeTest.KrxkClock
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

        global_obj.add_video_to_list(video)


def ConvertListToStr(ul: list):
    result = str('')
    for item in ul:
        result += str(item[0]) + ';'
    result = result[:-1]
    return result


def SaveToFile():
    df = pd.DataFrame(columns=['category', 'ID', 'length', 'comment', 'like', 'watch', 'share', 'name', 'user_list'])
    for i, video in enumerate(global_obj.GlobalVideoList):
        df.loc[i + 2] = [video.category, video.uid, video.length, video.comment, video.like, video.watch, video.share,
                         video.name, ConvertListToStr(video.user_list)]

    df.to_csv(file_path, encoding='utf-8', index=False)
    print('save to file done')
