class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        s = n =0
        while s<target or (s-target)%2:
            n+=1
            s+=n
        return n