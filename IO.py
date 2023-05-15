import pandas as pd
from GlobalVariable import global_obj


def ReadFromFile():
    from Video import Video
    data = pd.read_csv('Data.csv')
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
        user_id_list = str(row['user_list']).split(',')

        for user_id in user_id_list:
            if user_id == '':
                continue
            video.new_user(int(user_id), 0, False, False, False)  # 考虑隐私与复杂度问题，文件不存储用户行为信息（时长、点赞、评论等），该功能仅在内存实现

        global_obj.add_video_to_list(video)


def ConvertListToStr(ul: list):
    result = str('')
    for item in ul:
        result = str(item) + ','
    # result[-1] = ''
    return result


def SaveToFile():
    df = pd.DataFrame(columns=['category', 'ID', 'length', 'comment', 'like', 'watch', 'share', 'name', 'user_list'])
    for i, video in enumerate(global_obj.get_video_list_by_category(1)):
        df.loc[i + 2] = [video.category, video.uid, video.length, video.comment, video.like, video.watch, video.share,
                         video.name, ConvertListToStr(video.user_list)]

    df.to_csv('Data.csv', encoding='utf-8', index=False)
