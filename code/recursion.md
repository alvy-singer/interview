递归recursion  
根据'书上'的定义是函数调用自身  
使用场景是: 找到基本的应用单元, 然后递归下去  
这样说起来比较抽象, 据实际的例子可以帮助理解  
比较经典的两个例子是: 阶乘和费波拉契数列  
阶乘的写法如下:  
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
```
这个例子比较简单, 比较容易理解  
n=1时, 结果为1  
n=2时, 结果等于2*1=2  
n=3时, 结果等于3*2*1=6  
n=4时, 结果等于4*3*2*1=24  
...
n=n时, 结果等于n乘以n-1的阶乘  
  
接下来我们看一个更复杂一点的例子:  
不重复的字符串'abcdefg', 所有字母都多少种排列组合?  
我们还是从简单到复杂举例:  
字符串words为'a'时, 结果为['a']  
字符串words为'ab'时, 结果为['ba', 'ab']  
字符串words为'abc'时, 结果为['cba', 'bca', 'bac']和['cab', 'acb', 'abc']的合集  
...
字符串words为'abcdefg'时, 结果为最后一个字符'g'和之前的字符'abcdef'的结果做某种计算的结果  
有一点绕口, 'abcdef'的排列组合是一个元素为字符串的list, 'g'和其中的每一个字符串做排列组合(插入到字符串的每一个位置),  
得到一个list, 将所有list合并到一起就是'abcdefg'的排列组合结果  
这个计算方法如下所示:  
```python
def merge(words_list, word):
    result = []
    for words in words_list:
        zh_list = []
        len_words = len(words)
        for i in range(len_words+1):
            new_words = words[:i] + word + words[i:]
            zh_list.append(new_words)
        result.extend(zh_list)
    return result
```
那么排列组合的代码则可以写成:  
```python
def zh(words):
    if len(words) <= 1:
        return [words]
    return merge(zh(words[:-1]), words[-1])
```
这样我们可以对阶乘有了进一步的理解  
阶乘有一个最小单元, 和一个运算规则  
最小单元不适用于这个运算规则, 但是它起到结束作用, 不然会无限递归下去  
运算规则可以自己定义  
阶乘的例子我们可以换另外一种写法, 把计算规则(乘法)单独写出来, 能助于理解:  
```python
def plus(a, b):
    return a*b


def factorial(n):
    if n == 1:
        return 1
    return plus(factorial(n-1), n)
```
