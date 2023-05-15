import pandas as pd
import random
import User
import Video
from GlobalVariable import global_obj

# 读取Excel文件
data = pd.read_excel('Data.xlsx', nrows=10)


# 创建Video对象列表
def Read():
    print('Read start')
    for index, row in data.iterrows():
        video = Video.Video(
            category=row['category'],
            uid=row['ID'],
            length=row['length'],
            name=row['name'],
            like=row['like'],
            comment=row['comment'],
            share=row['share'],
            watch=row['watch'],
        )
        global_obj.add_video_to_list(video)
    for i, v in enumerate(global_obj.GlobalVideoList):
        print(i, v.comment)


def simulate_users():
    users = []

    for i in range(10000):
        # 随机生成用户的属性
        work_phase = random.randint(0, 4)
        gender = random.randint(0, 1)
        job = random.randint(0, 5)
        uid = i + 1  # 用户ID从1开始

        # 创建用户对象
        user = User.User(work_phase, gender, job, uid)

        # 将用户对象添加到列表中
        users.append(user)

    return users


Read()
