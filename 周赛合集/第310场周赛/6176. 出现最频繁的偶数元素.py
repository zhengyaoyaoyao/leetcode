import collections
from typing import List


class Solution1:
    def mostFrequentEven(self, nums: List[int]) -> int:
        res = [i for i in nums if i%2==0]
        if len(res)==0:
            return -1
        res.sort()
        curNum = 0
        maxNum=0
        result = res[0]
        for i in range(len(res)-1):
            if res[i]==res[i+1]:
                curNum+=1
            else:
                curNum=0
            if curNum>maxNum:
                result = res[i]
                maxNum = max(curNum,maxNum)
        return result

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # 先搞出字典，然后从字典里面找到最多出现的，然后当最多出现有很多的时候再找一个最小的值
        cnt = collections.Counter(x for x in nums if x % 2 == 0)
        if len(cnt)==0:
            return -1
        max_Value = max(cnt.values())
        return min(x for x,c in cnt.items() if c ==max_Value)

if __name__ == '__main__':
    nums = [29,47,21,41,13,37,25,7]
    test = Solution()
    print(test.mostFrequentEven(nums))

