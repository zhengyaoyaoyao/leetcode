from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def check(nums,value):
            for num in nums:
                if value&num!=0:
                    return False
            return True
        if len(nums)==1:
            return 1
        Maxlength = 1
        for slow in range(len(nums)):
            curMax= 1
            curValue=[nums[slow]]
            for quick in range(slow+1,len(nums)):
                if check(curValue,nums[quick]):
                    curValue.append(nums[quick])
                    curMax+=1
                else:
                    break
            Maxlength = max(curMax,Maxlength)
        return Maxlength
'''
暴力枚举优化，其实如果是按位与的话，多个与可以让前面的数先或，这样不断得叠加效果也是一样得。
然后其实枚举得话，跳出循环得时候就是不满足条件，这时候得quick和slow的差距其实已经就是最大的了，所以不用每次查完+1
'''

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        Maxlength = 0
        for i ,or_ in enumerate(nums):
            j =  i-1
            while j>=0 and (or_ &nums[i])==0:
                or_ |= nums[j]
                j-=1
            #这时候退出的i-j就是满足条件的最长子串了
            Maxlength = max(Maxlength,i-j)
        return Maxlength

'''
双指针，位运算。
'''
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = or_ =0
        for right ,x in enumerate(nums):
            while or_ &x :
                or_ ^=nums[left]
                left+=1
            or_ |=x
            ans = max(ans,right-left+1)
        return ans


if __name__ == '__main__':
    nums = [904163577,321202512,470948612,490925389,550193477,87742556,151890632,655280661,4,263168,32,573703555,886743681,937599702,120293650,725712231,257119393]
    test = Solution()
    print(test.longestNiceSubarray(nums))