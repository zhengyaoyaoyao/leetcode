import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(self.nums)
        self.k = k

    # 用最小堆，只要堆内留下k个，那么堆顶就肯定是第K大的值
    def add(self, val: int) -> int:
        #这种方法就不用每次去sort排序。
        heapq.heappush(self.nums,val)
        while len(self.nums) >self.k:
            heapq.heappop(self.nums)
        return self.nums[0]



if __name__ == '__main__':
    nums = [4, 5, 8, 2]
    heapq.heapify(nums)
    print(f'heapif后：{nums}')# 这个heap是以树的形式维护这个heap，所以并不是数组中就是以sort为顺序
    heapq.heappop(nums)
    print(f'pop后是否改变nums{nums}')#改变了，所以多几次pop就会变少。