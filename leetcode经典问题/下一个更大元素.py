
#一般模式：找到数组中下一个更大元素的坐标。返回这个坐标的数组
import collections
from typing import List

'''
经典问题就是返回一个下一个更大值的集合
例子一：维护的是一个对应的值
'''
#这是维护了一个哈希表
def nextGreaderElement(nums:List[int]) ->List[int]:
    #存放结果哈希表。有key和value
    res={}
    #维护一个栈
    stack =[]
    for num in reversed(nums):
        while stack and num>=stack[-1]:
            stack.pop()
        res[num] = stack[-1] if stack else -1
        stack.append(num)
    #这个res就是字典集合，
    return res
'''
例子二：维护的是更大值的和自己的下标差距
'''
#经典问题如果维护的是一个索引,得到的res是下一次更大数的索引。
def nextGreaderElement1(nums:List[int]) ->List[int]:
    res=[0]*len(nums)
    stack =[]
    for i in range(len(nums)):
        j = len(nums)-i-1
        while stack and nums[j]>=nums[stack[-1]]:
            stack.pop()
        res[j]=stack[-1]-j if stack else -1
        stack.append(j)
    return res
'''
例子三：如果是一个循环数组，即可以反过来一圈的，那么就把长度*2就好了
'''
def nextGreaderElement2(nums:List[int]) ->List[int]:
    n = len(nums)
    res=[0]*n
    stack=[]
    for i in range(2*n):
        j=2*n-i-1
        while stack and nums[j%n]>=stack[-1]:
            stack.pop()
        res[j%n]= stack[-1]  if stack else -1
        stack.append(nums[j%n])
    return res

if __name__ == '__main__':
    test=[1,3,4,2]
    # n = len(test)
    # for i in range(2*n):
    #     j=2*n-i-1
    #     print(j)
    print(nextGreaderElement2(test))
    # stack=[]