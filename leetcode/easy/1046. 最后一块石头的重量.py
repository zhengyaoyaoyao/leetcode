import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h= []
        for i in range(len(stones)):
            heapq.heappush(h,-stones[i])
        # 构建完成最大堆
        while len(h)>1:
            x1 = -heapq.heappop(h) #x1 先出比较大
            x2 = -heapq.heappop(h)
            if x1 == x2:
                continue
            else :
                heapq.heappush(h,x2-x1)
        if len(h) ==0:
            return 0
        else:
            return -h[0]

if __name__ == '__main__':
    stores= [2,7,4,1,8,1]
    test = Solution()
    print(test.lastStoneWeight(stores))