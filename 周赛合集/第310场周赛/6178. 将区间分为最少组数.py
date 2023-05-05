from heapq import heapreplace, heappush
from math import inf
from typing import List
'''
从零开始思考
1. 找到一个合理的顺序方便我们讨论把当前的区间放在哪个组
2. 答案/划分与输入的顺序无关 =》排序
3. 需要一个数据结构做到：找最小的+更新最小的值
4. 最小堆
'''


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        h = []
        for left,right in intervals:
            if h and left>h[0]:
                heapreplace(h,right) # 加到这个组的末尾 heap move down
            else:
                heappush(h,right)
        return len(h)
if __name__ == '__main__':
    test = Solution()
    intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
    print(test.minGroups(intervals))