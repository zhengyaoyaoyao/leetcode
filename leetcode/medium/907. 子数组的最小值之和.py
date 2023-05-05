from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 用单调栈算出左右最小值坐标的边界，然后只要在这个范围内，有几个值就有几次的贡献
        n ,ans = len(arr),0
        l,r = [-1]*n,[n]*n;# 定义两个单调栈
        stack = [] #作为单调栈
        for i in range(n):
            while stack and arr[stack[-1]]>=arr[i]:
                r[stack.pop()]=i
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>arr[i]:
                l[stack.pop()]=i
            stack.append(i)

        for i in range(n):
            a,b = i-l[i],r[i]-i
            ans +=a*b*arr[i]
        return ans %(10**9+7)
