'''
1. 如果是降序，那么就是最大，直接输出。
2. 最简单的就是把最大的放在前面。
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list()
        numCopy=num
        while numCopy!=0:
            nums.append(numCopy%10)
            numCopy=int(numCopy/10)
        nums.reverse()
        changeIndex=0
        for index,value in enumerate(nums):
            if value>=max(nums[index:]):
                continue
            else:
                changeIndex=index
                break
        curNums= nums[changeIndex:]
        maxValue=0
        maxIndex=0
        for i in range(len(curNums)):
            if curNums[i]>=maxValue:
                maxIndex=i
                maxValue = curNums[i]
        nums[changeIndex],nums[changeIndex+maxIndex]=nums[changeIndex+maxIndex],nums[changeIndex]
        res =''
        for i in nums:
            res+=str(i)
        return int(res)







if __name__ == '__main__':
    nums = 9973
    test = Solution()
    print(test.maximumSwap(nums))