class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        checkSet = {'a','e','i','o','u','A','E','I','O','U'}
        ans=0
        for i in range(len(s)//2):
            right = i+len(s)//2
            if s[i] in checkSet:
                ans+=1
            if s[right] in checkSet:
                ans-=1
        if ans != 0:
            return False
        return True