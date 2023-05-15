import pandas as pd
import random
import User
import Video
from GlobalVariable import global_obj

# 读取Excel文件
data = pd.read_csv('Data.csv', nrows=10)


# 创建Video对象列表
def ReadFromFile():
    for index, row in data.iterrows():
        video = Video.Video(
            category=int(row['category']),
            uid=int(row['ID']),
            length=int(row['length']),
            name=row['name'],
            like=int(row['like']),
            comment=int(row['comment']),
            share=int(row['share']),
            watch=int(row['watch']),
        )
        user_id_list = str(row['user_list']).split(',')
        for user_id in user_id_list:
            video.new_user(int(user_id), 0, False, False, False)

        global_obj.add_video_to_list(video)

    videos = global_obj.GlobalVideoList
    

    for v in videos:
        print(v.uid, v.name, v.user_list)


ReadFromFile()
