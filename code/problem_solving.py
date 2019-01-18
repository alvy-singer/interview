def time_angle(hour, minute, second):
    """时间时针分针的夹角
    """
    assert 0 <= hour <= 24, '时格式不正确'
    assert 0 <= minute <= 60, '分格式不正确'
    assert 0 <= second <= 60, '秒格式不正确'
    hour = hour - 12 if hour > 12 else hour
    hour_angle = 360 * ((hour*60 + minute)*60+second)/(12*60*60)
    minute_angle = 360 * minute / 60
    result = abs(hour_angle-minute_angle)
    return result - 360 if result >= 360 else result


def binary_search(my_list, start_index=0):
    """
    一个有序的数字序列, 经过循环移动之后, 找到转折的地方
    例如列表[1, 2, 3, 4, 5], 移动之后变成[3, 4, 5, 1, 2], 找到峰值也就是5的索引

    Args:
        my_list: 不能为空, 从小到大排列可经过移动的list
    """
    len_my_list = len(my_list)
    if my_list[0] <= my_list[-1]:
        return start_index + len_my_list - 1
    mid_index = len_my_list // 2
    left = my_list[:mid_index]
    right = my_list[mid_index:]
    if right[0] > right[-1]:
        return binary_search(right, start_index + mid_index)
    else:
        return binary_search(left, start_index)
