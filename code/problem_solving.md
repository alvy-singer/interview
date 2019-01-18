在面试的时候拿到试题我往往都是一脸懵逼  
不要慌, 解题也是有方法的, 一般解题的思路有5种:  
1. 举例法
##### question
求钟表时针和分针的夹角  
##### 思路
1点钟的时候, 时针指向1, 分针指向12, 角度是360/12, 相当于时针相对于12点的角度  
1点30分30秒的时候, 时针在1和2的中间, 分针指向30, 现在时针分针都不在12点钟方向, 那么我们可以这么计算, 角度是分针相对于12点的角度, 减去时针相对于12点的角度  
那么问题就变成了计算时针分针相对于12点方向的角度  
分针相对于12点方向的角度是360 * (30/60), 因为一圈是60分钟360°  
时针相对于12点方向的角度要复杂一些了, 不是360 * (1/12), 因为1点30分的时候时针不是指向1点
计算方法应该是360 * ((1 * 60 + 30)*60+30)/(12 * 60 * 60), 将时间换算成秒
##### 答案
```python
def time_angle(hour, minute, second):
    assert 0 <= hour <= 24, '时格式不正确'
    assert 0 <= minute <= 60, '分格式不正确'
    assert 0 <= second <= 60, '秒格式不正确'
    hour = hour - 12 if hour > 12 else hour
    hour_angle = 360 * ((hour*60 + minute)*60+second)/(12*60*60)
    minute_angle = 360 * minute / 60
    result = abs(hour_angle-minute_angle)
    return result - 360 if result >= 360 else result
```
2. 套用模式法
##### question
一个有序的数字序列, 经过循环移动之后, 找到转折的地方  
例如列表[1, 2, 3, 4, 5], 移动之后变成[3, 4, 5, 1, 2], 找到峰值也就是5的索引
似曾相识对不对, 和二分法搜索类似, 只是现在要找到拐点的位置, 而不是特点的某个点
实现方法是:
```python
def binary_search(my_list, start_index=0):
    len_my_list = len(my_list)
    if my_list[0] <= my_list[-1]:
        return start_index + len_my_list - 1
    mid_index = len_my_list // 2
    left = my_list[:mid_index]
    right = my_list[mid_index:]
    if right[0] > right[-1]:
        return binary_search(right, istart_index + mid_index)
    else:
        return binary_search(left, start_index)
```
如果有序list第一个元素小于最后一个元素, 说明list没有经过移动, 最后一个元素就是最大的元素  
如果相等, 则代表list为空或者只有一个元素, 则返回0  
如果不是, 则把list分成两半, 如果右半部分第一个元素大于最后一个元素, 说明拐点在右半部分, 如果不是, 说明拐点在左半部分,
分别调用自身就可以了.
