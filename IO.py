import pandas as pd
import random
import User
import Video
from GlobalVariable import global_obj

# 读取Excel文件
data = pd.read_csv('Data.csv', nrows=10, encoding='utf-8')


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


def SaveToFile():
    df = pd.DataFrame(columns=['category', 'ID', 'length', 'comment', 'like', 'watch', 'share', 'name', 'user_list'])
    df.loc[2] = [0, 1, 112, 4916, 11380, 1750690, 4847, '洗衣机在家很闷，改装一下出去溜溜', "4191,5778"]

    # df_insert = pd.DataFrame([])
    # df_insert.columns = ['category', 'ID', 'length,comment', 'like', 'watch', 'share', 'name', 'user_list']
    # df = pd.concat([df, df_insert], ignore_index=True, axis=0)

    df.to_csv('2.csv', encoding='utf-8', index=False)


# ReadFromFile()
SaveToFile()
