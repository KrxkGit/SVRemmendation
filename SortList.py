# coding=utf-8

# 利用融合排序算法进行排序，降序排列，其中传入vl元素结构为：[视频uid, 视频weight]
def VideoListSort(vl: list):
    key_col = 1  # 权重位置
    if len(vl) > 1:
        mid = len(vl) // 2

        left_arr = vl[:mid]
        right_arr = vl[mid:]

        VideoListSort(left_arr)
        VideoListSort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i][key_col] > right_arr[j][key_col]:
                vl[k] = left_arr[i]
                i += 1
            else:
                vl[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            vl[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            vl[k] = right_arr[j]
            j += 1
            k += 1
