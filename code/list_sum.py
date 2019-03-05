import copy 


def list_two_sum(my_list, n):
    """my_list里和为n的两个元素的列表
    """
    result = []
    for i, v in enumerate(my_list):
        if n-v in my_list[i+1:]:
            result.append([v, n-v])
    return result


def helper(my_list, pre_result):
    """
    """
    two_dict = {}
    result = []
    for item in pre_result:
        for i in item:
            if i in two_dict:
                two_result = two_dict.get(i)
            else:
                cal_list = [t for t in my_list if t not in item]
                two_result = list_two_sum(cal_list, i)
            if two_result:
                copy_item = copy.deepcopy(item)
                copy_item.remove(i)
                for two_item in two_result:
                    append_item = sorted(copy_item+two_item)
                    if append_item not in result:
                        result.append(append_item)
    return result


def list_sum(my_list, n, count):
    """求my_list和为n, 数量为count子序列

    假设my_list是有序的
    """
    if count == 2:
        return list_two_sum(my_list, n)
    return helper(my_list, list_sum(my_list, n, count-1))
