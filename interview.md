# Python开发工程师如何换工作  

> 准确的说, 应该叫后端开发工程师, 而不应该叫Python开发工程师, Python只是开发的手段和语言之一

## 换工作的思考

换工作的原因有很多种,例如现在的工作不开心, 想要更高的收入等等

但是无论哪一种原因, 我需要想清楚以后的职业规划, life is short, 一份不顺利的工作花费无效的时间精力不说, 也会影响到职业生涯

所以换工作是一件大事, 不能着急, 意气用事, 否则得不偿失

## 工作机会

几种方式:
- 拉勾
- 猎聘
- 内推
- 各类论坛
  v2ex等

## 简历

如何写简历着了不在赘述
需要注意是:
1. 仔细检查格式和文字, 不求花哨漂亮的版式, 但是要结构清晰, 不要有错别字
2. 简历上的每一个点, 自己要做到胸有成竹, 因为面试官不了解你, 只能从简历上的点来问你, 如果你答不上来, 扣分会比较多

## 参考资料

<https://github.com/jwasham/coding-interview-university>
<https://github.com/taizilongxu/interview_python>
<https://book.douban.com/subject/25753386/>

## 面试准备

> 以[程序员面试金典]()来做准备, 所以这里的内容相当于这本书的读书笔记

### 面试流程
### 面试揭秘
### 特殊情况
### 面试之前
### 行为面试题
### 技术面试题

#### 算法题的五种解法

在面试的时候拿到试题往往都是一脸懵逼  
不要慌, 解题也是有方法的, 一般解题的思路有5种:  
1. 举例法
- question
求钟表时针和分针的夹角  
- 思路
1点钟的时候, 时针指向1, 分针指向12, 角度是360/12, 相当于时针相对于12点的角度  
1点30分30秒的时候, 时针在1和2的中间, 分针指向30, 现在时针分针都不在12点钟方向, 那么我们可以这么计算, 角度是分针相对于12点的角度, 减去时针相对于12点的角度  
那么问题就变成了计算时针分针相对于12点方向的角度  
分针相对于12点方向的角度是360 * (30/60), 因为一圈是60分钟360°  
时针相对于12点方向的角度要复杂一些了, 不是360 * (1/12), 因为1点30分的时候时针不是指向1点
计算方法应该是360 * ((1 * 60 + 30)*60+30)/(12 * 60 * 60), 将时间换算成秒
- 答案
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
- question
一个有序的数字序列, 经过循环移动之后, 找到转折的地方  
例如列表[1, 2, 3, 4, 5], 移动之后变成[3, 4, 5, 1, 2], 找到峰值也就是5的索引
- 思路
似曾相识对不对, 和二分法搜索类似, 只是现在要找到拐点的位置, 而不是特点的某个点
- 答案
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

### 录用通知及其他
### 面试考题
### 解题技巧
