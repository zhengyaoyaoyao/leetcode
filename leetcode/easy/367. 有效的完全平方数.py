class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left<= right:
            mid = left +right>>1
            if mid*mid==num:
                return True
            if mid*mid <num:
                left = mid+1
            if mid*mid >num:
                right = mid-1
        return False

if __name__ == '__main__':
    num =14
    test = Solution()
    print(test.isPerfectSquare(num))