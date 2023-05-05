class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        check =list(str(x))
        left = 0
        right=len(check)-1
        while left<right:
            if check[left] == check[right]:
                left+=1
                right-=1
            else:
                return False
        return True


if __name__ == '__main__':
    test=Solution()
    print(test.isPalindrome(1231231))