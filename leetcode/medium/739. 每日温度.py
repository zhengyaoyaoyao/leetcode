from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res= [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            j=len(temperatures)-1-i
            while stack and temperatures[j]>=temperatures[stack[-1]]:
                stack.pop()
            res[j]=stack[-1]-j if stack else 0
            stack.append(j)
        return res