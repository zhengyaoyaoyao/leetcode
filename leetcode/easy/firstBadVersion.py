# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def isBadVersion(self,version:int)->bool:
        pass
    def firstBadVersion(self, n: int) -> int:
        left=1
        right = n
        while left<=right:
            mid = (left+right)>>1
            if self.isBadVersion(mid):
                #True就是错误版本，最小的应该在左侧
                right=mid
            else:
                left=mid+1
        return int(left)
